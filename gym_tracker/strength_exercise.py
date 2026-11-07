from gym_tracker.exercise import Exercise
from gym_tracker.progressable import Progressable


class StrengthExercise(Exercise, Progressable):
    """A weighted exercise measured in sets, reps and kilograms."""

    MIN_REPS = 1
    MAX_REPS = 30
    MAX_WEIGHT_KG = 300
    WEIGHT_INCREMENT_KG = 2.5
    CALORIES_PER_REP = 0.4
    WEIGHT_FACTOR = 100

    def __init__(
        self, name: str, sets: int, reps: int, weight_kg: float,
        muscle_groups=()
    ) -> None:
        super().__init__(name, sets, muscle_groups)

        if isinstance(reps, int) and self.MIN_REPS <= reps <= self.MAX_REPS:
            self.__reps = reps
        else:
            print(f"Invalid reps for {self.name}, using {self.MIN_REPS}")
            self.__reps = self.MIN_REPS

        if (
            isinstance(weight_kg, (int, float))
            and 0 <= weight_kg <= self.MAX_WEIGHT_KG
        ):
            self.__weight_kg = weight_kg
        else:
            print(f"Invalid weight for {self.name}, using bodyweight (0kg)")
            self.__weight_kg = 0

    @property
    def reps(self) -> int:
        return self.__reps

    @property
    def weight_kg(self) -> float:
        return self.__weight_kg

    def volume(self) -> float:
        # Training volume is the total weight moved in the exercise.
        return self._sets * self.__reps * self.__weight_kg

    def calculate_calories(self) -> float:
        # Heavier lifts burn more per rep, so weight scales the base
        # rate.
        weight_bonus = 1 + self.__weight_kg / self.WEIGHT_FACTOR
        return self._sets * self.__reps * self.CALORIES_PER_REP * weight_bonus

    def describe(self) -> str:
        return (
            f"{self.name}: {self._sets} x {self.__reps} "
            f"@ {self.__weight_kg}kg"
        )

    def progress(self) -> str:
        if self.__weight_kg + self.WEIGHT_INCREMENT_KG > self.MAX_WEIGHT_KG:
            return f"{self.name} is already at the maximum weight"
        self.__weight_kg += self.WEIGHT_INCREMENT_KG
        return f"{self.name} increased to {self.__weight_kg}kg"