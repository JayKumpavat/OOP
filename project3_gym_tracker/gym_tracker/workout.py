from gym_tracker.exercise import Exercise
from gym_tracker.gym_exceptions import (
    DuplicateExerciseError,
    EmptyWorkoutError,
    WorkoutCompletedError,
    WorkoutFullError,
)
from gym_tracker.progressable import Progressable


class Workout:
    """One training session made up of exercises.

    A Workout is created and owned by a Member (composition). The
    exercises are created separately and only collected by the workout
    (aggregation), so the same exercise can be reused in a later
    session.
    """

    MAX_EXERCISES = 12

    def __init__(self, title: str, date: str) -> None:
        self.__title = title
        self.__date = date
        self.__exercises = []
        self.__completed = False

    @property
    def exercises(self) -> list:
        return list(self.__exercises)

    @property
    def completed(self) -> bool:
        return self.__completed

    def add_exercise(self, exercise: Exercise) -> bool:
        # Every rule is checked before the list changes, so a failed
        # add leaves the workout exactly as it was.
        if not isinstance(exercise, Exercise):
            print("Only Exercise objects can be added to a workout")
            return False
        if self.__completed:
            raise WorkoutCompletedError(self.__title)
        if exercise in self.__exercises:
            raise DuplicateExerciseError(self.__title, exercise.name)
        if len(self.__exercises) >= self.MAX_EXERCISES:
            raise WorkoutFullError(self.__title, self.MAX_EXERCISES)
        self.__exercises.append(exercise)
        return True

    def complete(self) -> bool:
        if self.__completed:
            raise WorkoutCompletedError(self.__title)
        if len(self.__exercises) == 0:
            raise EmptyWorkoutError(self.__title)
        self.__completed = True
        return True

    def total_calories(self) -> float:
        # Each exercise calculates its own calories, so the workout
        # never needs to know which concrete type it is holding.
        total = 0
        for exercise in self.__exercises:
            total += exercise.calculate_calories()
        return total

    def muscles_trained(self) -> set:
        # Union of every exercise's muscle groups, so each muscle
        # appears once however many exercises target it.
        return {
            muscle
            for exercise in self.__exercises
            for muscle in exercise.muscle_groups
        }

    def shared_muscles(self, other: "Workout") -> set:
        # Intersection shows which muscles two sessions both worked,
        # which helps spot training the same area two days in a row.
        if not isinstance(other, Workout):
            print("Can only compare with another Workout")
            return set()
        return self.muscles_trained() & other.muscles_trained()

    def progress_exercises(self) -> list:
        # Only exercises that implement the Progressable interface are
        # asked to progress.
        results = []
        for exercise in self.__exercises:
            if isinstance(exercise, Progressable):
                results.append(exercise.progress())
        return results

    def __str__(self) -> str:
        status = "done" if self.__completed else "in progress"
        lines = [f"{self.__title} on {self.__date} ({status})"]
        for exercise in self.__exercises:
            lines.append(f"  - {exercise}")
        lines.append(f"  Total: ~{self.total_calories():.1f} kcal")
        return "\n".join(lines)