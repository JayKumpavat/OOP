from necromancy_game.warrior_undead import WarriorUndead


class SkeletonWarrior(WarriorUndead):
    """A reanimated skeleton soldier."""

    SUMMON_NAME = "Undead Skeleton Warrior"
    STARTING_HEALTH = 40
    STARTING_POWER = 12
    MIN_HEALTH = 20
    MAX_HEALTH = 120
    MIN_POWER = 5
    MAX_POWER = 40
    HEALTH_PER_LEVEL = 12
    POWER_PER_LEVEL = 4

    def __init__(self, unit_id: int) -> None:
        super().__init__(
            unit_id, self.SUMMON_NAME, self.STARTING_HEALTH,
            self.STARTING_POWER
        )