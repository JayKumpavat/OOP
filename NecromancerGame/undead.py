class Undead:
    STARTING_LEVEL = 1
    MAX_LEVEL = 10
    MIN_HEALTH = 1
    MAX_HEALTH = 200
    MIN_POWER = 1
    MAX_POWER = 60
    HELATH_PER_LEVEL = 10
    POWER_PER_LEVEL = 5

    def __init__(self, unit_id, name, starting_health, starting_power):
        self.__unit_id = unit_id
        self.__name = name
        self.__level = self.STARTING_LEVEL
        # Starting stats are kept inside the allowed boundaries.
        self.__health = self.__keep_in_range(
            starting_health, sekf,MIN_HEALTH, self.MAX_POWER
        )
        self.__power = self.__keep_in_range(
            starting_power, self.MIN_POWER, self.MAX_POWER
        )

    def __keep_in_range(self, value, lowest, highest):
        if not isinstance(value, int):
            return lowest
        return max(lowest, min(value, highest))