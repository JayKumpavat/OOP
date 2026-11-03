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

    def __init__(self, name: str, sets: int) -> None:
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

    @property
    def name(self) -> str:
        return self.__name

    @property
    def sets(self) -> int:
        return self._sets

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