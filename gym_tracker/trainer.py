from gym_tracker.person import Person


class Trainer(Person):
    """A personal trainer who coaches a limited number of members."""

    MAX_CLIENTS = 5

    def __init__(self, name: str, person_id: int, specialty: str) -> None:
        super().__init__(name, person_id)
        self.__specialty = specialty
        self.__client_count = 0

    @property
    def specialty(self) -> str:
        return self.__specialty

    @property
    def client_count(self) -> int:
        return self.__client_count

    def has_space(self) -> bool:
        return self.__client_count < self.MAX_CLIENTS

    def take_on_client(self) -> bool:
        if not self.has_space():
            print(f"{self.name} is fully booked")
            return False
        self.__client_count += 1
        return True

    def release_client(self) -> bool:
        if self.__client_count == 0:
            return False
        self.__client_count -= 1
        return True

    def role_summary(self) -> str:
        return (
            f"Trainer ({self.__specialty}), "
            f"{self.__client_count}/{self.MAX_CLIENTS} clients"
        )