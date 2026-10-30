from NecromancerGame.undead import Undead


class CursedUndead(Undead):
    """Undead that fight with supernatural curses instead of weapons."""

    def __init__(
        self, unit_id: int, name: str, starting_health: int,
        starting_power: int
    ) -> None:
        super().__init__(unit_id, name, starting_health, starting_power)
        self.__curses_cast = 0

    @property
    def curses_cast(self) -> int:
        return self.__curses_cast

    def command(self) -> str:
        self.__curses_cast += 1
        return (
            f"{super().command()} It casts a withering curse for "
            f"{self._power} damage."
        )