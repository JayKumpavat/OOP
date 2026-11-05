from gym_tracker.exercise import Exercise
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
    def title(self) -> str:
        return self.__title

    @property
    def date(self) -> str:
        return self.__date

    @property
    def exercises(self) -> list:
        return list(self.__exercises)

    @property
    def completed(self) -> bool:
        return self.__completed

    def add_exercise(self, exercise: Exercise) -> bool:
        if self.__completed:
            print(f"{self.__title} is finished, it cannot be changed")
            return False
        if not isinstance(exercise, Exercise):
            print("Only Exercise objects can be added to a workout")
            return False
        if exercise in self.__exercises:
            print(f"{exercise.name} is already in {self.__title}")
            return False
        if len(self.__exercises) >= self.MAX_EXERCISES:
            print(f"{self.__title} already has the maximum exercises")
            return False
        self.__exercises.append(exercise)
        return True

    def complete(self) -> bool:
        if self.__completed or len(self.__exercises) == 0:
            print(f"{self.__title} cannot be completed")
            return False
        self.__completed = True
        return True

    def total_calories(self) -> float:
        # Each exercise calculates its own calories, so the workout
        # never needs to know which concrete type it is holding.
        total = 0
        for exercise in self.__exercises:
            total += exercise.calculate_calories()
        return total

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