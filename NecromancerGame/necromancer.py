from NecromancerGame.resource_pool import ResourcePool
from NecromancerGame.summoning_ritual import SummoningRitual
from NecromancerGame.undead import Undead

class Necromancer:
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