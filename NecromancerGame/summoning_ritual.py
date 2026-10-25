from NecromancerGame.resource_pool import ResourcePool
from NecromancerGame.undead import Undead

class SummoningRitual:
    MIN_ECTOPLASM_COST = 1

    def __init__(
        self, 
        ritual_name: str,
        summon_name: str,
        starting_health: int,
        starting_power: int,
        necrotic_cost: int = 0,
        spirit_cost: int = 0,
        bone_cost: int = 0,
        flesh_cost: int = 0,
        ectoplasm_cost: int = MIN_ECTOPLASM_COST
        ) -> None:

        self.__ritual_name = ritual_name
        self.__summon_name = summon_name
        self.__starting_health = starting_health
        self.__starting_power = starting_power
        self.__necrotic_cost = necrotic_cost
        self.__spirit_cost = spirit_cost
        self.__bone_cost = bone_cost
        self.__flesh_cost = flesh_cost

        # Every ritual must use Ectoplasm.
        if (
            isinstance(ectoplasm_cost, int)
            and ectoplasm_cost >= self.MIN_ECTOPLASM_COST
        ):
            self.__ectoplasm_cost = ectoplasm_cost
        else:
            print(f"{ritual_name} must cost Ectoplasm, using the minimum")
            self.__ectoplasm_cost = self.MIN_ECTOPLASM_COST

    @property
    def ritual_name(self) -> str:
        return self.__ritual_name

    @property
    def summon_name(self) -> str:
        return self.__summon_name

    @property
    def starting_health(self) -> int:
        return self.__starting_health

    @property
    def starting_power(self) -> int:
        return self.__starting_power

    @property
    def necrotic_cost(self) -> int:
        return self.__necrotic_cost

    @property
    def spirit_cost(self) -> int:
        return self.__spirit_cost

    @property
    def bone_cost(self) -> int:
        return self.__bone_cost

    @property
    def flesh_cost(self) -> int:
        return self.__flesh_cost

    @property
    def ectoplasm_cost(self) -> int:
        return self.__ectoplasm_cost

    def can_perform(self, resources: ResourcePool) -> bool:
        if not isinstance(resources, ResourcePool):
            print("A ritual needs a valid ResourcePool")
            return False
        return resources.has_resources(
            self.__necrotic_cost, self.__spirit_cost, self.__bone_cost,
            self.__flesh_cost, self.__ectoplasm_cost
        )

    def consume_resources(self, resources: ResourcePool) -> bool:
        if not self.can_perform(resources):
            return False
        return resources.spend(
            self.__necrotic_cost, self.__spirit_cost, self.__bone_cost,
            self.__flesh_cost, self.__ectoplasm_cost
        )
        