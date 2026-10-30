from necromancy_game.undead import Undead


class PutridZombie(Undead):
    """A slow but durable rotting corpse."""

    SUMMON_NAME = "Putrid Zombie"
    STARTING_HEALTH = 60
    STARTING_POWER = 8
    MIN_HEALTH = 30
    MAX_HEALTH = 160
    MIN_POWER = 4
    MAX_POWER = 30
    HEALTH_PER_LEVEL = 15
    POWER_PER_LEVEL = 2

    def __init__(self, unit_id: int) -> None:
        super().__init__(
            unit_id, self.SUMMON_NAME, self.STARTING_HEALTH,
            self.STARTING_POWER
        )

    def command(self) -> str:
        return f"{super().command()} It shambles forward and spreads rot."