class ResourcePool:
    """Stores and manges the magical resources used for summoning.

    Quantities can only change through collect() and spend(). Every
    value is checked before anything changes, so a failed operation
    leaves all exisiting values exactly the same.
    """
    MINIMUM_QUANTITY = 0

    def __init__(self, necrotic_runes, spirit_runes, bone_runes, flesh_runes, ectoplasm):
        self.__necrotic_runes = MINIMUM_QUANTITY
        self.__spirit_runes = MINIMUM_QUANTITY
        self.__bone_runes = MINIMUM_QUANTITY
        self.__flesh_runes = MINIMUM_QUANTITY
        self.__ectoplasm = MINIMUM_QUANTITY

        if not self.collect(necrotic_runes, spirit_runes, bone_runes, flesh_runes, ectoplasm):
            print("The resource pool will start empty")

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

    def has_resources(self, necrotic_runes, spirit_runes, bone_runes, flesh_runes, ectoplasm):
        if not self.__all_valid(necrotic_runes, spirit_runes, bone_runes, flesh_runes, ectoplasm):
            return False

        return (
            self.__necrotic_runes >= necrotic_runes
            and self.__spirit_runes >= spirit_runes
            and self.__bone_runes >= bone_runes
            and self.__flesh_runes >= flesh_runes
            and self.__ectoplasm >= ectoplasm
        )

    def spend(self, necrotic_runes, spirit_runes, bone_runes, flesh_runes, ectoplasm):
        if not self.has_resources(necrotic_runes, spirit_runes, bone_runes, flesh_runes, ectoplasm):
            return False
        
        self.__necrotic_runes -= necrotic_runes
        self.__spirit_runes -= spirit_runes
        self.__bone_runes -= bone_runes
        self.__flesh_runes -= flesh_runes
        self.__ectoplasm -= ectoplasm
        return True

    def __is_valid_quantity(self, quantity):
        return (
            isinstance(quantity, int)
            and not isinstance(quantity, bool)
            and quantity >= self.MINIMUM_QUANTITY
        )

    def __all_valid(self, necrotic_runes, spirit_runes, bone_runes, flesh_runes, ectoplasm):
        return (
            self.__is_valid_quantity(necrotic_runes)
            and self.__is_valid_quantity(spirit_runes)
            and self.__is_valid_quantity(bone_runes)
            and self.__is_valid_quantity(flesh_runes)
            and self.__is_valid_quantity(ectoplasm)
        )

    def __str__(self):
        return (
            f"Necrotic: {self.__necrotic_runes}"
            f"Spirit: {self.__spirit_runes}"
            f"Bone: {self.__bone_runes}"
            f"Flesh: {self.__flesh_runes}"
            f"Ectoplasm: {self.__ectoplasm}"
        )