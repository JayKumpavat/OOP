from NecromancerGame.resource_pool import ResourcePool
from NecromancerGame.undead import Undead

class SummoningRitual:
    MIN_ECTOPLASM_COST = 1

    def __init__(self, ritual_name, summon_name, starting_health, starting_power, necrotic_cost, spirit_cost, bone_cost, flesh_cost, ectoplasm_cost: int = MIN_ECTOPLASM_COST):
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

        