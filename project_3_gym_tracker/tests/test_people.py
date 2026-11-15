"""Tests for Person, Member and Trainer."""
import pytest

from gym_tracker.exercise import Exercise
from gym_tracker.gym_exceptions import TrainerFullError
from gym_tracker.member import Member
from gym_tracker.person import Person
from gym_tracker.trainer import Trainer


class TestPerson:
    def test_person_cannot_be_created_directly(self):
        with pytest.raises(TypeError):
            Person("Someone", 1)

    def test_invalid_name_and_id_use_defaults(self):
        member = Member("", -4, "Get fit")
        assert member.name == "Unknown"
        assert member.person_id == 0

    def test_people_with_the_same_id_are_equal(self, member):
        assert member == Member("Different name", 101, "Other goal")

    def test_person_is_not_equal_to_other_types(self, member):
        assert member != 101

    def test_str_uses_role_summary_polymorphically(self, member, trainer):
        assert str(member).startswith("#101 Jay - Member, goal: Build")
        assert str(trainer) == "#201 Lee - Trainer (Powerlifting), 0/5 clients"


class TestTrainer:
    def test_take_on_client(self, trainer):
        assert trainer.take_on_client() is True
        assert trainer.client_count == 1

    def test_full_trainer_rejects_clients(self, full_trainer):
        assert full_trainer.has_space() is False
        with pytest.raises(TrainerFullError, match="maximum of 5") as info:
            full_trainer.take_on_client()
        assert info.value.trainer_name == "Ava"
        assert full_trainer.client_count == Trainer.MAX_CLIENTS

    def test_release_client(self, full_trainer):
        assert full_trainer.release_client() is True
        assert full_trainer.has_space()

    def test_release_with_no_clients(self, trainer):
        assert trainer.release_client() is False
        assert trainer.client_count == 0


class TestMemberTrainer:
    def test_assign_trainer(self, member, trainer):
        assert member.assign_trainer(trainer) is True
        assert member.trainer == trainer
        assert trainer.client_count == 1

    def test_assign_same_trainer_twice(self, member, trainer):
        member.assign_trainer(trainer)
        assert member.assign_trainer(trainer) is False
        assert trainer.client_count == 1

    def test_assign_non_trainer(self, member):
        assert member.assign_trainer("Lee") is False
        assert member.trainer is None

    def test_full_trainer_leaves_member_unchanged(
        self, member, trainer, full_trainer
    ):
        member.assign_trainer(trainer)
        with pytest.raises(TrainerFullError):
            member.assign_trainer(full_trainer)
        assert member.trainer == trainer
        assert trainer.client_count == 1

    def test_switching_trainer_frees_old_spot(self, member, trainer):
        other = Trainer("Ava", 202, "Endurance")
        member.assign_trainer(trainer)
        assert member.assign_trainer(other) is True
        assert trainer.client_count == 0
        assert other.client_count == 1

    def test_remove_trainer(self, member, trainer):
        member.assign_trainer(trainer)
        assert member.remove_trainer() is True
        assert member.trainer is None
        assert trainer.client_count == 0

    def test_remove_trainer_when_none(self, member):
        assert member.remove_trainer() is False

    def test_role_summary_names_trainer(self, member, trainer):
        member.assign_trainer(trainer)
        assert "coached by Lee" in member.role_summary()


class TestMemberWorkouts:
    def test_start_workout_is_owned_by_member(self, member):
        workout = member.start_workout("Leg Day", "2026-10-22")
        assert member.workouts == [workout]

    def test_only_completed_workouts_count(self, member, full_workout):
        member.start_workout("Planned", "2026-10-30")
        assert member.completed_workout_count() == 0
        assert member.total_calories() == 0
        full_workout.complete()
        assert member.completed_workout_count() == 1
        assert member.total_calories() == pytest.approx(224.23)

    def test_muscles_trained_and_untrained(self, member, full_workout):
        full_workout.complete()
        trained = {"chest", "arms", "shoulders", "legs"}
        assert member.muscles_trained() == trained
        assert member.untrained_muscles() == Exercise.MUSCLE_GROUPS - trained

    def test_incomplete_workouts_do_not_count_as_trained(
        self, member, full_workout
    ):
        assert member.muscles_trained() == set()
        assert member.untrained_muscles() == Exercise.MUSCLE_GROUPS


class TestMemberHandlesWorkoutErrors:
    """Member catches workout exceptions so the program can carry on."""

    def test_add_to_workout(self, member, workout, squat):
        assert member.add_to_workout(workout, squat) is True
        assert workout.exercises == [squat]

    def test_duplicate_is_handled(self, member, full_workout, bench_press):
        assert member.add_to_workout(full_workout, bench_press) is False
        assert len(full_workout.exercises) == 3

    def test_completed_workout_is_handled(self, member, full_workout, squat):
        member.finish_workout(full_workout)
        assert member.add_to_workout(full_workout, squat) is False
        assert squat not in full_workout.exercises

    def test_cannot_use_another_members_workout(self, workout, squat):
        other = Member("Sam", 102, "Improve fitness")
        assert other.add_to_workout(workout, squat) is False
        assert other.finish_workout(workout) is False
        assert workout.exercises == []

    def test_finish_workout(self, member, full_workout):
        assert member.finish_workout(full_workout) is True
        assert member.completed_workout_count() == 1

    def test_finish_empty_workout_is_handled(self, member, workout):
        assert member.finish_workout(workout) is False
        assert member.completed_workout_count() == 0