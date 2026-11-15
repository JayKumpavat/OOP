"""Tests for Workout and its collection of exercises."""
import pytest

from gym_tracker.gym_exceptions import (
    DuplicateExerciseError,
    EmptyWorkoutError,
    GymError,
    WorkoutCompletedError,
    WorkoutError,
    WorkoutFullError,
)
from gym_tracker.mobility_exercise import MobilityExercise
from gym_tracker.strength_exercise import StrengthExercise
from gym_tracker.workout import Workout


class TestAddingExercises:
    def test_add_exercise_keeps_order(self, workout, bench_press, stretch):
        assert workout.add_exercise(bench_press) is True
        assert workout.add_exercise(stretch) is True
        assert workout.exercises == [bench_press, stretch]

    def test_duplicate_exercise_is_rejected(self, full_workout):
        copy = StrengthExercise("BENCH PRESS", 1, 1, 20)
        with pytest.raises(DuplicateExerciseError, match="already in") as info:
            full_workout.add_exercise(copy)
        assert info.value.exercise_name == "BENCH PRESS"
        assert len(full_workout.exercises) == 3

    def test_non_exercise_is_rejected(self, workout):
        assert workout.add_exercise("Plank") is False
        assert workout.exercises == []

    def test_cannot_go_past_maximum(self, workout):
        for number in range(Workout.MAX_EXERCISES):
            workout.add_exercise(MobilityExercise(f"Drill {number}", 1, 30))
        extra = MobilityExercise("One too many", 1, 30)
        with pytest.raises(WorkoutFullError, match="at most 12"):
            workout.add_exercise(extra)
        assert len(workout.exercises) == Workout.MAX_EXERCISES

    def test_exercises_list_is_a_copy(self, full_workout, squat):
        full_workout.exercises.append(squat)
        assert squat not in full_workout.exercises


class TestCompleting:
    def test_complete_workout(self, full_workout):
        assert full_workout.complete() is True
        assert full_workout.completed

    def test_empty_workout_cannot_be_completed(self, workout):
        with pytest.raises(EmptyWorkoutError, match="Push Day") as info:
            workout.complete()
        assert info.value.workout_title == "Push Day"
        assert not workout.completed

    def test_workout_cannot_be_completed_twice(self, full_workout):
        full_workout.complete()
        with pytest.raises(WorkoutCompletedError):
            full_workout.complete()

    def test_completed_workout_cannot_change(self, full_workout, squat):
        full_workout.complete()
        with pytest.raises(WorkoutCompletedError, match="cannot change"):
            full_workout.add_exercise(squat)
        assert squat not in full_workout.exercises

    def test_workout_errors_share_parents(self, full_workout):
        full_workout.complete()
        # Both parent classes catch the same problem.
        with pytest.raises(WorkoutError):
            full_workout.complete()
        with pytest.raises(GymError):
            full_workout.complete()


class TestCalculations:
    def test_total_calories_adds_every_exercise(self, full_workout):
        assert full_workout.total_calories() == pytest.approx(
            20.48 + 200 + 3.75)

    def test_empty_workout_has_no_calories(self, workout):
        assert workout.total_calories() == 0

    def test_progress_only_affects_progressable(self, full_workout):
        results = full_workout.progress_exercises()
        assert results == [
            "Bench Press increased to 62.5kg",
            "Treadmill Run increased to 25 min",
        ]

    def test_str_lists_exercises_and_total(self, full_workout):
        text = str(full_workout)
        assert text.startswith("Push Day on 2026-10-20 (in progress)")
        assert "Treadmill Run" in text
        assert text.endswith("Total: ~224.2 kcal")

    def test_str_shows_done_when_completed(self, full_workout):
        full_workout.complete()
        assert "(done)" in str(full_workout)


class TestMuscleSets:
    def test_muscles_trained_is_a_union(self, full_workout):
        assert full_workout.muscles_trained() == {
            "chest", "arms", "shoulders", "legs"}

    def test_shared_muscles_is_an_intersection(
        self, full_workout, member, squat
    ):
        leg_day = member.start_workout("Leg Day", "2026-10-22")
        leg_day.add_exercise(squat)
        assert full_workout.shared_muscles(leg_day) == {"legs"}

    def test_shared_muscles_with_non_workout(self, full_workout):
        assert full_workout.shared_muscles("Leg Day") == set()