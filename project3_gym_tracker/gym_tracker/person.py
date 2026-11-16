from abc import ABC, abstractmethod

class Person(ABC):
    """Common details for anyone registered at the gym.

    Person is abstract because the gym only ever registers a specific
    kind of person (a member or a trainer), never a plain "person".
    """

    def __init__(self, name: str, person_id: int) -> None:
        if isinstance(name, str) and name.strip() != "":
            self.__name = name.strip()
        else:
            print("Invalid name, using 'Unknown'")
            self.__name = "Unknown"

        if isinstance(person_id, int) and person_id > 0:
            self.__person_id = person_id
        else:
            print("Invalid id, it must be a positive integer")
            self.__person_id = 0

    @property
    def name(self) -> str:
        return self.__name

    @property
    def person_id(self) -> int:
        return self.__person_id

    @abstractmethod
    def role_summary(self) -> str:
        pass

    def __eq__(self, other) -> bool:
        if not isinstance(other, Person):
            return False
        return self.__person_id == other.person_id

    def __str__(self) -> str:
        return f"#{self.__person_id} {self.__name} - {self.role_summary()}"