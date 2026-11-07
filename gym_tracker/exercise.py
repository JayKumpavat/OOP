from abc import ABC, abstractmethod


class Exercise(ABC):
    """The general idea of an exercise.

    Exercise is abstract because "an exercise" on its own has no way to
    work out calories or describe itself. Each concrete exercise type
    must provide calculate_calories() and describe(), which lets a
    Workout treat every exercise the same way (polymorphism).
    """

    MIN_SETS = 1
    MAX_SETS = 10
    MUSCLE_GROUPS = {
        "chest", "back", "shoulders", "arms", "core", "legs", "glutes",
    }

    def __init__(self, name: str, sets: int, muscle_groups=()) -> None:
        if isinstance(name, str) and name.strip() != "":
            self.__name = name.strip()
        else:
            print("Invalid exercise name, using 'Unnamed exercise'")
            self.__name = "Unnamed exercise"

        if isinstance(sets, int) and self.MIN_SETS <= sets <= self.MAX_SETS:
            self._sets = sets
        else:
            print(f"Invalid sets for {self.__name}, using {self.MIN_SETS}")
            self._sets = self.MIN_SETS

        # A set is used because a muscle is either targeted or not, so
        # duplicates have no meaning and membership checks are fast.
        self.__muscle_groups = set()
        for muscle in muscle_groups:
            self.add_muscle_group(muscle)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def sets(self) -> int:
        return self._sets

    @property
    def muscle_groups(self) -> set:
        # A copy is returned so the set cannot be changed from outside.
        return set(self.__muscle_groups)

    def add_muscle_group(self, muscle: str) -> bool:
        if not isinstance(muscle, str):
            print("Muscle groups must be given as text")
            return False
        muscle = muscle.strip().lower()
        if muscle not in self.MUSCLE_GROUPS:
            print(f"'{muscle}' is not a recognised muscle group")
            return False
        self.__muscle_groups.add(muscle)
        return True

    def targets(self, muscle: str) -> bool:
        return muscle in self.__muscle_groups

    @abstractmethod
    def calculate_calories(self) -> float:
        pass

    @abstractmethod
    def describe(self) -> str:
        pass

    def __eq__(self, other) -> bool:
        # The same exercise type with the same name counts as a
        # duplicate inside a workout, even if the numbers are different.
        if not isinstance(other, Exercise):
            return False
        return (
            type(self) is type(other)
            and self.__name.lower() == other.name.lower()
        )

    def __str__(self) -> str:
        return f"{self.describe()} (~{self.calculate_calories():.1f} kcal)"