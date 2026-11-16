from necromancy_game.cursed_undead import CursedUndead


class VengefulGhost(CursedUndead):
    """A restless spirit that curses the living."""

    SUMMON_NAME = "Vengeful Ghost"
    STARTING_HEALTH = 30
    STARTING_POWER = 18
    MIN_HEALTH = 15
    MAX_HEALTH = 90
    MIN_POWER = 10
    MAX_POWER = 60
    HEALTH_PER_LEVEL = 8
    POWER_PER_LEVEL = 6

    def __init__(self, unit_id: int) -> None:
        super().__init__(
            unit_id, self.SUMMON_NAME, self.STARTING_HEALTH,
            self.STARTING_POWER
        )