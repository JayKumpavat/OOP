from gym_tracker.exercise import Exercise


class MobilityExercise(Exercise):
    """A stretch or mobility drill held for a number of seconds.

    It is an Exercise but not Progressable, because flexibility work is
    about doing it regularly rather than making it heavier.
    """

    MIN_HOLD_SECONDS = 10
    MAX_HOLD_SECONDS = 120
    CALORIES_PER_MINUTE = 2.5
    SECONDS_PER_MINUTE = 60

    def __init__(
        self, name: str, sets: int, hold_seconds: int, muscle_groups=()
    ) -> None:
        super().__init__(name, sets, muscle_groups)

        if (
            isinstance(hold_seconds, int)
            and self.MIN_HOLD_SECONDS <= hold_seconds
            <= self.MAX_HOLD_SECONDS
        ):
            self.__hold_seconds = hold_seconds
        else:
            print(f"Invalid hold time for {self.name}, using "
                  f"{self.MIN_HOLD_SECONDS}s")
            self.__hold_seconds = self.MIN_HOLD_SECONDS

    @property
    def hold_seconds(self) -> int:
        return self.__hold_seconds

    def calculate_calories(self) -> float:
        minutes = self._sets * self.__hold_seconds / self.SECONDS_PER_MINUTE
        return minutes * self.CALORIES_PER_MINUTE

    def describe(self) -> str:
        return f"{self.name}: {self._sets} x {self.__hold_seconds}s hold"