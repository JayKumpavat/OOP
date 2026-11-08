from gym_tracker.member import Member
from gym_tracker.trainer import Trainer


class Gym:
    """A gym that registers members and trainers.

    Members and trainers are stored in dictionaries keyed by their id,
    because the gym looks people up by membership number rather than by
    position. The people still exist without the gym (aggregation).
    """

    def __init__(self, name: str) -> None:
        self.__name = name
        self.__members = {}
        self.__trainers = {}

    @property
    def name(self) -> str:
        return self.__name

    @property
    def members(self) -> dict:
        # A copy is returned so outside code cannot add or remove
        # members without going through the gym's rules.
        return dict(self.__members)

    def register_member(self, member: Member) -> bool:
        if not isinstance(member, Member):
            print("Only Member objects can be registered as members")
            return False
        if member.person_id in self.__members:
            print(f"Member id {member.person_id} is already registered")
            return False
        self.__members[member.person_id] = member
        return True

    def register_trainer(self, trainer: Trainer) -> bool:
        if not isinstance(trainer, Trainer):
            print("Only Trainer objects can be registered as trainers")
            return False
        if trainer.person_id in self.__trainers:
            print(f"Trainer id {trainer.person_id} is already registered")
            return False
        self.__trainers[trainer.person_id] = trainer
        return True

    def is_member(self, member_id: int) -> bool:
        return member_id in self.__members

    def find_member(self, member_id: int) -> Member:
        return self.__members.get(member_id)

    def find_trainer(self, trainer_id: int) -> Trainer:
        return self.__trainers.get(trainer_id)

    def remove_member(self, member_id: int) -> bool:
        member = self.__members.pop(member_id, None)
        if member is None:
            print(f"No member with id {member_id} is registered")
            return False
        # The trainer's spot is freed so it can go to someone else.
        member.remove_trainer()
        return True

    def assign_trainer(self, member_id: int, trainer_id: int) -> bool:
        member = self.find_member(member_id)
        trainer = self.find_trainer(trainer_id)
        if member is None or trainer is None:
            print("Both the member and trainer must be registered")
            return False
        return member.assign_trainer(trainer)

    def members_coached_by(self, trainer_id: int) -> list:
        trainer = self.find_trainer(trainer_id)
        if trainer is None:
            return []
        return [
            member for member in self.__members.values()
            if member.trainer == trainer
        ]

    def calories_by_member(self) -> dict:
        return {
            member.name: member.total_calories()
            for member in self.__members.values()
        }

    def __str__(self) -> str:
        return (
            f"{self.__name}: {len(self.__members)} member(s), "
            f"{len(self.__trainers)} trainer(s)"
        )