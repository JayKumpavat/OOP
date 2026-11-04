from gym_tracker.exercise import Exercise
from gym_tracker.progressable import Progressable


class CardioExercise(Exercise, Progressable):
    """A timed exercise such as running, rowing or cycling."""

    MIN_MINUTES = 1
    MAX_MINUTES = 180
    MINUTE_INCREMENT = 5
    LOW_INTENSITY = 1
    HIGH_INTENSITY = 3
    CALORIES_PER_MINUTE = 5

    def __init__(
        self, name: str, sets: int, minutes_per_set: int, intensity: int
    ) -> None:
        super().__init__(name, sets)

        if (
            isinstance(minutes_per_set, int)
            and self.MIN_MINUTES <= minutes_per_set <= self.MAX_MINUTES
        ):
            self.__minutes_per_set = minutes_per_set
        else:
            print(f"Invalid minutes for {self.name}, using "
                  f"{self.MIN_MINUTES}")
            self.__minutes_per_set = self.MIN_MINUTES

        if (
            isinstance(intensity, int)
            and self.LOW_INTENSITY <= intensity <= self.HIGH_INTENSITY
        ):
            self.__intensity = intensity
        else:
            print(f"Invalid intensity for {self.name}, using low")
            self.__intensity = self.LOW_INTENSITY

    @property
    def minutes_per_set(self) -> int:
        return self.__minutes_per_set

    @property
    def intensity(self) -> int:
        return self.__intensity

    def total_minutes(self) -> int:
        return self._sets * self.__minutes_per_set

    def calculate_calories(self) -> float:
        return (
            self.total_minutes() * self.CALORIES_PER_MINUTE
            * self.__intensity
        )

    def describe(self) -> str:
        return (
            f"{self.name}: {self._sets} x {self.__minutes_per_set} min "
            f"(intensity {self.__intensity}/{self.HIGH_INTENSITY})"
        )

    def progress(self) -> str:
        if self.__minutes_per_set + self.MINUTE_INCREMENT > self.MAX_MINUTES:
            return f"{self.name} is already at the maximum duration"
        self.__minutes_per_set += self.MINUTE_INCREMENT
        return f"{self.name} increased to {self.__minutes_per_set} min"