class ResourcePool:
    MINIMUM_QUANTITY = 0

    def __init__(self, necrotic_runes, spirit_runes, bone_runes, flesh_runes, ectoplasm):
        self.__necrotic_runes = MINIMUM_QUANTITY
        self.__spirit_runes = MINIMUM_QUANTITY
        self.__bone_runes = MINIMUM_QUANTITY
        self.__flesh_runes = MINIMUM_QUANTITY
        self.__ectoplasm = MINIMUM_QUANTITY
        