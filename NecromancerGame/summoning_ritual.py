from NecromancerGame.resource_pool import ResourcePool
from NecromancerGame.undead import Undead

class SummoningRitual:
    """Describes what a ritual costs and which undead it creates.

    The ritual knows its own requirements, but it never changes resource
    quantities itself. It asks the ResourcePool to check and spend them.
    """

    MIN_ECTOPLASM_COST = 1

    def __init__(
        self,
        ritual_name: str,
        summon_class,
        necrotic_cost: int = 0,
        spirit_cost: int = 0,
        bone_cost: int = 0,
        flesh_cost: int = 0,
        ectoplasm_cost: int = MIN_ECTOPLASM_COST,
    ) -> None:
        self.__ritual_name = ritual_name
        self.__summon_class = summon_class
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
        return self.__summon_class.SUMMON_NAME

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

    def create_summon(self, unit_id: int) -> Undead:
        return self.__summon_class(unit_id)

    def __str__(self) -> str:
        return (
            f"{self.__ritual_name} -> {self.summon_name} | Cost: "
            f"Necrotic {self.__necrotic_cost}, Spirit {self.__spirit_cost}, "
            f"Bone {self.__bone_cost}, Flesh {self.__flesh_cost}, "
            f"Ectoplasm {self.__ectoplasm_cost}"
        )