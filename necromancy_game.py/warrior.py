from NecromancerGame.undead import Undead

class WarriorUndead(Undead):
    """Undead that fights with wepons and armour in direct comabt"""

    def __init__(
        self, unit_id: int, name: str, starting_health: int,
        starting_power: int
    ) -> None:
        super().__init__(unit_id, name, starting_health, starting_power)
        self.__battles_fought = 0

    @property
    def battles_fought(self) -> int:
        return self.__battles_fought

    def command(self) -> str:
        self.__battles_fought += 1
        return (
            f"{super().command()} It charges in and strikes with its "
            f"blade for {self._power} damage."
        )

    def combat_style(self) -> str:
        return "Martial - direct melee combat with weapon and armour"