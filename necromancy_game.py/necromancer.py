from necromancy_game.resource_pool import ResourcePool
from necromancy_game.summoning_ritual import SummoningRitual
from necromancy_game.undead import Undead

class Necromancer:
    """Coordinates resources, rituals and the controlled undead army.

    The Necromancer creates and owns its ResourcePool (composition),
    keeps a list of the undead it controls (aggregation) and uses
    rituals to summon them (dependency). It delegates every state change
    to the object responsible for it.
    """

    MAX_UNDEAD = 6
    FIRST_UNIT_ID = 1

    def __init__(
        self,
        name: str,
        necrotic_runes: int = 0,
        spirit_runes: int = 0,
        bone_runes: int = 0,
        flesh_runes: int = 0,
        ectoplasm: int = 0,
    ) -> None:
        self.__name = name
        self.__resources = ResourcePool(
            necrotic_runes, spirit_runes, bone_runes, flesh_runes, ectoplasm
        )
        self.__undead = []
        self.__next_unit_id = self.FIRST_UNIT_ID

    @property
    def name(self) -> str:
        return self.__name

    @property
    def resource_summary(self) -> str:
        return str(self.__resources)

    @property
    def army(self) -> list:
        return list(self.__undead)

    def collect_resources(
        self,
        necrotic_runes: int = 0,
        spirit_runes: int = 0,
        bone_runes: int = 0,
        flesh_runes: int = 0,
        ectoplasm: int = 0,
    ) -> bool:
        return self.__resources.collect(
            necrotic_runes, spirit_runes, bone_runes, flesh_runes, ectoplasm
        )

    def summon(self, ritual: SummoningRitual) -> Undead:
        if not isinstance(ritual, SummoningRitual):
            print("Only a SummoningRitual can be performed")
            return None

        if len(self.__undead) >= self.MAX_UNDEAD:
            print(f"{self.__name} cannot control more than "
                  f"{self.MAX_UNDEAD} undead")
            return None

        if not ritual.consume_resources(self.__resources):
            print(f"Not enough resources to perform {ritual.ritual_name}")
            return None

        summoned = ritual.create_summon(self.__next_unit_id)
        self.__next_unit_id += 1
        self.__undead.append(summoned)
        return summoned

    def dismiss(self, unit_id: int) -> bool:
        undead = self.__find_undead(unit_id)
        if undead is None:
            print(f"No undead with id {unit_id} is under control")
            return False
        self.__undead.remove(undead)
        return True

    def level_undead(self, unit_id: int) -> bool:
        undead = self.__find_undead(unit_id)
        if undead is None:
            print(f"No undead with id {unit_id} is under control")
            return False
        return undead.level_up()

    def command_undead(self, unit_id: int) -> str:
        undead = self.__find_undead(unit_id)
        if undead is None:
            return f"No undead with id {unit_id} is under control"
        return undead.command()

    def command_army(self) -> list:
        # Each undead responds with its own overridden command().
        orders = []
        for undead in self.__undead:
            orders.append(undead.command())
        return orders

    def describe_undead(self, unit_id: int) -> str:
        undead = self.__find_undead(unit_id)
        if undead is None:
            return f"No undead with id {unit_id} is under control"
        return str(undead)

    def __find_undead(self, unit_id: int) -> Undead:
        for undead in self.__undead:
            if undead.unit_id == unit_id:
                return undead
        return None

    def __str__(self) -> str:
        lines = [
            f"Necromancer {self.__name} "
            f"({len(self.__undead)}/{self.MAX_UNDEAD} undead)",
            f"Resources: {self.__resources}",
        ]
        for undead in self.__undead:
            lines.append(f"  {undead}")
        return "\n".join(lines)