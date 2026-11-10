"""Tests for the Gym and its member and trainer dictionaries."""
import pytest

from gym_tracker.member import Member
from gym_tracker.trainer import Trainer


class TestRegistering:
    def test_members_are_keyed_by_id(self, gym, member):
        assert gym.members[101] is member
        assert sorted(gym.members) == [101, 102]

    def test_duplicate_member_id_is_rejected(self, gym):
        copy = Member("Copy", 101, "Duplicate")
        assert gym.register_member(copy) is False
        assert gym.members[101].name == "Jay"

    def test_non_member_is_rejected(self, gym, trainer):
        assert gym.register_member(trainer) is False
        assert not gym.is_member(201)

    def test_register_trainer(self, gym):
        coach = Trainer("Ava", 202, "Endurance")
        assert gym.register_trainer(coach) is True
        assert gym.find_trainer(202) is coach

    def test_duplicate_trainer_id_is_rejected(self, gym):
        assert gym.register_trainer(Trainer("Copy", 201, "None")) is False

    def test_non_trainer_is_rejected(self, gym, member):
        assert gym.register_trainer(member) is False

    def test_members_dictionary_is_a_copy(self, gym):
        gym.members.clear()
        assert len(gym.members) == 2


class TestLookups:
    def test_is_member(self, gym):
        assert gym.is_member(102)
        assert not gym.is_member(999)

    def test_find_member(self, gym, member):
        assert gym.find_member(101) is member

    def test_find_missing_member(self, gym):
        assert gym.find_member(999) is None


class TestTrainerAssignment:
    def test_assign_trainer_by_id(self, gym, member, trainer):
        assert gym.assign_trainer(101, 201) is True
        assert member.trainer is trainer

    @pytest.mark.parametrize("member_id, trainer_id", [(999, 201),
                                                       (101, 999)])
    def test_assign_with_unknown_id(self, gym, member_id, trainer_id):
        assert gym.assign_trainer(member_id, trainer_id) is False

    def test_members_coached_by(self, gym):
        gym.assign_trainer(101, 201)
        gym.assign_trainer(102, 201)
        names = [member.name for member in gym.members_coached_by(201)]
        assert names == ["Jay", "Sam"]

    def test_members_coached_by_unknown_trainer(self, gym):
        assert gym.members_coached_by(999) == []


class TestRemovingAndTotals:
    def test_remove_member_frees_trainer(self, gym, trainer):
        gym.assign_trainer(101, 201)
        assert gym.remove_member(101) is True
        assert not gym.is_member(101)
        assert trainer.client_count == 0

    def test_remove_missing_member(self, gym):
        assert gym.remove_member(999) is False
        assert len(gym.members) == 2

    def test_calories_by_member(self, gym, full_workout):
        full_workout.complete()
        calories = gym.calories_by_member()
        assert calories["Jay"] == pytest.approx(224.23)
        assert calories["Sam"] == 0

    def test_str(self, gym):
        assert str(gym) == "Northside Strength Club: 2 member(s), 1 trainer(s)"


class TestExtraFixtures:
    """Tests that use the second fixture for each class."""

    def test_rower_calories_and_progress(self, rower):
        # Calories are 4 sets x 3 minutes x 5 kcal x intensity 3.
        assert rower.calculate_calories() == pytest.approx(180)
        assert rower.progress() == "Rowing Intervals increased to 8 min"
        assert rower.total_minutes() == 32

    def test_quad_stretch_calories(self, quad_stretch):
        assert quad_stretch.calculate_calories() == pytest.approx(3.75)
        assert quad_stretch.targets("legs")

    def test_coached_member_can_drop_trainer(self, coached_member, trainer):
        assert coached_member.remove_trainer() is True
        assert trainer.client_count == 0

    def test_coached_member_summary(self, coached_member):
        assert "coached by Lee" in str(coached_member)

    def test_empty_gym(self, empty_gym, member):
        assert str(empty_gym) == "Empty Gym: 0 member(s), 0 trainer(s)"
        assert empty_gym.calories_by_member() == {}
        assert empty_gym.register_member(member) is True
        assert empty_gym.is_member(101)