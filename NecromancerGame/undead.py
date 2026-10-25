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

    @property
    def unit_id(self):
        return self.__unit_id

    @property
    def name(self):
        return self.__name

    @property
    def level(self):
        return self.__level

    @property
    def health(self):
        return self.__health
    
    @property
    def power(self):
        return self.__power

    def level_up(self):
        if self.__level >= self.MAX_LEVEL:
            print(f"{self.__name} is already at the maximum level")
            return False
        
        self.__level += 1
        self.__health = min(
            self.__health + self.HELATH_PER_LEVEL, self.MAX_HEALTH
        )
        self.__power = min(
            self.__power + self.POWER_PER_LEVEL, self.MAX_POWER
        )
        return True

    def __keep_in_range(self, value, lowest, highest):
        if not isinstance(value, int):
            return lowest
        return max(lowest, min(value, highest))