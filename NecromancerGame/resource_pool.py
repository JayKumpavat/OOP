class ResourcePool:
    MINIMUM_QUANTITY = 0

    def __init__(self, necrotic_runes, spirit_runes, bone_runes, flesh_runes, ectoplasm):
        self.__necrotic_runes = MINIMUM_QUANTITY
        self.__spirit_runes = MINIMUM_QUANTITY
        self.__bone_runes = MINIMUM_QUANTITY
        self.__flesh_runes = MINIMUM_QUANTITY
        self.__ectoplasm = MINIMUM_QUANTITY

    @property
    def necrotic_runes(self):
        return self.__necrotic_runes

    @property
    def spirit_runes(self):
        return self.__spirit_runes

    @property
    def bone_runes(self):
        return self.__bone_runes

    @property
    def flesh_runes(self):
        return self.__flesh_runes

    @property
    def ectoplasm(self):
        return self.__ectoplasm

    def collect(self, necrotic_runes, spirit_runes, bone_runes, flesh_runes, ectoplasm):
        if not self.__all_valid(necrotic_runes, spirit_runes, bone_runes, flesh_runes, ectoplasm):
            print("Collection rejected, quantities must be a whole numbers 0+")
            return False

        self.__necrotic_runes += necrotic_runes
        self.__spirit_runes += spirit_runes
        self.__bone_runes += bone_runes
        self.__flesh_runes += flesh_runes
        self.__ectoplasm += ectoplasm
        return True