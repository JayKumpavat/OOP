"""Tests for the Exercise hierarchy and the Progressable interface."""
import pytest

from gym_tracker.cardio_exercise import CardioExercise
from gym_tracker.exercise import Exercise
from gym_tracker.mobility_exercise import MobilityExercise
from gym_tracker.progressable import Progressable
from gym_tracker.strength_exercise import StrengthExercise


class TestAbstractExercise:
    def test_exercise_cannot_be_created_directly(self):
        with pytest.raises(TypeError):
            Exercise("Plain exercise", 3)

    def test_progressable_cannot_be_created_directly(self):
        with pytest.raises(TypeError):
            Progressable()

    def test_str_uses_each_subclass_describe(self, bench_press, stretch):
        assert str(bench_press) == "Bench Press: 4 x 8 @ 60kg (~20.5 kcal)"
        assert str(stretch) == "Hamstring Stretch: 3 x 30s hold (~3.8 kcal)"

    def test_invalid_name_uses_default(self):
        exercise = MobilityExercise("   ", 2, 30)
        assert exercise.name == "Unnamed exercise"

    @pytest.mark.parametrize("sets", [0, 11, "3", 2.5])
    def test_invalid_sets_fall_back_to_minimum(self, sets):
        exercise = MobilityExercise("Stretch", sets, 30)
        assert exercise.describe() == "Stretch: 1 x 30s hold"

    @pytest.mark.parametrize("sets", [Exercise.MIN_SETS, Exercise.MAX_SETS])
    def test_set_boundaries_are_accepted(self, sets):
        exercise = MobilityExercise("Stretch", sets, 30)
        assert exercise.describe() == f"Stretch: {sets} x 30s hold"


class TestExerciseEquality:
    def test_same_type_and_name_are_equal(self, bench_press):
        other = StrengthExercise("bench press", 3, 10, 50)
        assert bench_press == other

    def test_different_types_are_not_equal(self):
        strength = StrengthExercise("Row", 3, 10, 40)
        cardio = CardioExercise("Row", 1, 10, 2)
        assert strength != cardio

    def test_non_exercise_is_not_equal(self, bench_press):
        assert bench_press != "Bench Press"


class TestMuscleGroups:
    def test_valid_groups_are_stored_once(self):
        exercise = StrengthExercise("Push Up", 3, 10, 0,
                                    ["chest", "Chest", " arms "])
        assert exercise.muscle_groups == {"chest", "arms"}

    def test_unknown_group_is_rejected(self, bench_press):
        assert bench_press.add_muscle_group("wings") is False
        assert "wings" not in bench_press.muscle_groups

    def test_non_text_group_is_rejected(self, bench_press):
        assert bench_press.add_muscle_group(7) is False

    def test_add_muscle_group(self, bench_press):
        assert bench_press.add_muscle_group("core") is True
        assert bench_press.targets("core")

    def test_targets_checks_membership(self, bench_press):
        assert bench_press.targets("chest")
        assert not bench_press.targets("legs")

    def test_returned_set_is_a_copy(self, bench_press):
        groups = bench_press.muscle_groups
        groups.add("legs")
        assert not bench_press.targets("legs")


class TestStrengthExercise:
    def test_calories_scale_with_weight(self, bench_press):
        # Calories are 4 sets x 8 reps x 0.4 kcal x (1 + 60 / 100).
        assert bench_press.calculate_calories() == pytest.approx(20.48)

    def test_volume_is_total_weight_moved(self, bench_press):
        assert bench_press.volume() == 4 * 8 * 60

    def test_progress_adds_weight(self, bench_press):
        result = bench_press.progress()
        assert result == "Bench Press increased to 62.5kg"
        assert bench_press.volume() == pytest.approx(4 * 8 * 62.5)

    def test_progress_stops_at_maximum_weight(self):
        lift = StrengthExercise("Leg Press", 3, 10, 300)
        assert lift.progress() == "Leg Press is already at the maximum weight"
        assert lift.volume() == 3 * 10 * 300

    @pytest.mark.parametrize("reps", [0, 31, "8"])
    def test_invalid_reps_fall_back_to_minimum(self, reps):
        lift = StrengthExercise("Curl", 2, reps, 10)
        assert lift.describe() == "Curl: 2 x 1 @ 10kg"

    @pytest.mark.parametrize("weight", [-1, 301, "heavy"])
    def test_invalid_weight_uses_bodyweight(self, weight):
        lift = StrengthExercise("Dip", 3, 10, weight)
        assert lift.volume() == 0


class TestCardioExercise:
    def test_calories_use_minutes_and_intensity(self, treadmill):
        assert treadmill.calculate_calories() == pytest.approx(200)

    def test_total_minutes(self):
        rower = CardioExercise("Rower", 4, 3, 3)
        assert rower.total_minutes() == 12

    def test_progress_adds_minutes(self, treadmill):
        assert treadmill.progress() == "Treadmill Run increased to 25 min"
        assert treadmill.total_minutes() == 25

    def test_progress_stops_at_maximum_duration(self):
        ride = CardioExercise("Ride", 1, 180, 1)
        assert ride.progress() == "Ride is already at the maximum duration"
        assert ride.total_minutes() == 180

    @pytest.mark.parametrize("minutes", [0, 181, "20"])
    def test_invalid_minutes_fall_back_to_minimum(self, minutes):
        run = CardioExercise("Run", 1, minutes, 2)
        assert run.total_minutes() == 1

    @pytest.mark.parametrize("intensity", [0, 4, "high"])
    def test_invalid_intensity_falls_back_to_low(self, intensity):
        run = CardioExercise("Run", 1, 10, intensity)
        assert run.describe() == "Run: 1 x 10 min (intensity 1/3)"


class TestMobilityExercise:
    def test_calories_use_hold_time(self, stretch):
        # Calories are 3 sets x 30 seconds = 1.5 minutes x 2.5 kcal.
        assert stretch.calculate_calories() == pytest.approx(3.75)

    def test_is_not_progressable(self, stretch):
        assert not isinstance(stretch, Progressable)

    @pytest.mark.parametrize("seconds", [9, 121, "30"])
    def test_invalid_hold_falls_back_to_minimum(self, seconds):
        stretch = MobilityExercise("Quad Stretch", 2, seconds)
        assert stretch.describe() == "Quad Stretch: 2 x 10s hold"


class TestPolymorphism:
    def test_every_exercise_answers_the_same_calls(
        self, bench_press, treadmill, stretch
    ):
        # The test never checks the concrete type, it only uses the
        # shared Exercise interface.
        exercises = [bench_press, treadmill, stretch]
        calories = [exercise.calculate_calories() for exercise in exercises]
        assert calories == pytest.approx([20.48, 200, 3.75])
        assert all(exercise.describe() for exercise in exercises)