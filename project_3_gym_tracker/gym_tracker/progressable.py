from abc import ABC, abstractmethod


class Progressable(ABC):
    """Interface for anything that can be made harder over time.

    It holds no state, only the method an exercise must provide if it
    supports progressive overload. Not every exercise is progressable (a
    stretch is not made "heavier"), so this is kept separate from
    Exercise instead of forcing every exercise to implement it.
    """

    @abstractmethod
    def progress(self) -> str:
        pass