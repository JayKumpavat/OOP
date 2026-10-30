class Undead:
    """The general summoned creature that every undead type is built
    from.

    Undead holds the identifier, name, statistics and levelling
    behaviour shared by all summons. Stat limits and growth are class
    constants, so each subclass only needs to redefine the numbers that
    make it different and the inherited level_up() uses them
    automatically.
    """

    STARTING_LEVEL = 1
    MAX_LEVEL = 10
    MIN_HEALTH = 1
    MAX_HEALTH = 100
    MIN_POWER = 1
    MAX_POWER = 50
    HEALTH_PER_LEVEL = 10
    POWER_PER_LEVEL = 5

    def __init__(
        self, unit_id: int, name: str, starting_health: int,
        starting_power: int
    ) -> None:
        self.__unit_id = unit_id
        self.__name = name
        self._level = self.STARTING_LEVEL
        # Starting stats are kept inside this type's boundaries.
        self._health = self.__keep_in_range(
            starting_health, self.MIN_HEALTH, self.MAX_HEALTH
        )
        self._power = self.__keep_in_range(
            starting_power, self.MIN_POWER, self.MAX_POWER
        )

    @property
    def unit_id(self) -> int:
        return self.__unit_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def level(self) -> int:
        return self._level

    @property
    def health(self) -> int:
        return self._health

    @property
    def power(self) -> int:
        return self._power

    def level_up(self) -> bool:
        if self._level >= self.MAX_LEVEL:
            print(f"{self.__name} is already at the maximum level")
            return False

        self._level += 1
        self._health = min(
            self._health + self.HEALTH_PER_LEVEL, self.MAX_HEALTH
        )
        self._power = min(self._power + self.POWER_PER_LEVEL, self.MAX_POWER)
        return True

    def command(self) -> str:
        return f"{self.__name} #{self.__unit_id} rises and obeys."

    def __keep_in_range(self, value: int, lowest: int, highest: int) -> int:
        if not isinstance(value, int):
            return lowest
        return max(lowest, min(value, highest))

    def __str__(self) -> str:
        return (
            f"#{self.__unit_id} {self.__name} (Lv {self._level}/"
            f"{self.MAX_LEVEL}) HP {self._health}/{self.MAX_HEALTH} "
            f"PWR {self._power}/{self.MAX_POWER}"
        )
        
    def combat_style(self) -> str:
        return "Cursed - supernatural attacks that drain life from afar"