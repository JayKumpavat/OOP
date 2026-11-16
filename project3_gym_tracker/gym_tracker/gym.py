from gym_tracker.gym_exceptions import (
    GymError,
    MemberNotFoundError,
    TrainerNotFoundError,
)
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
        if member_id not in self.__members:
            raise MemberNotFoundError(member_id)
        return self.__members[member_id]

    def find_trainer(self, trainer_id: int) -> Trainer:
        if trainer_id not in self.__trainers:
            raise TrainerNotFoundError(trainer_id)
        return self.__trainers[trainer_id]

    def remove_member(self, member_id: int) -> bool:
        try:
            member = self.find_member(member_id)
        except MemberNotFoundError as error:
            print(f"Could not remove member. {error}")
            return False
        del self.__members[member_id]
        # The trainer's spot is freed so it can go to someone else.
        member.remove_trainer()
        return True

    def assign_trainer(self, member_id: int, trainer_id: int) -> bool:
        # Any lookup or capacity problem is handled here, so the caller
        # gets a simple True or False and the program carries on.
        try:
            member = self.find_member(member_id)
            trainer = self.find_trainer(trainer_id)
            return member.assign_trainer(trainer)
        except GymError as error:
            print(f"Could not assign trainer. {error}")
            return False

    def members_coached_by(self, trainer_id: int) -> list:
        try:
            trainer = self.find_trainer(trainer_id)
        except TrainerNotFoundError as error:
            print(error)
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