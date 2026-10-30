from necromancy_game.warrior_undead import WarriorUndead


class PhantomGuardian(WarriorUndead):
    """A spectral knight that shields the necromancer."""

    SUMMON_NAME = "Phantom Guardian"
    STARTING_HEALTH = 70
    STARTING_POWER = 10
    MIN_HEALTH = 40
    MAX_HEALTH = 180
    MIN_POWER = 5
    MAX_POWER = 35
    HEALTH_PER_LEVEL = 18
    POWER_PER_LEVEL = 3

    def __init__(self, unit_id: int) -> None:
        super().__init__(
            unit_id, self.SUMMON_NAME, self.STARTING_HEALTH,
            self.STARTING_POWER
        )