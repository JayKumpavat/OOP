from necromancy_game.cursed_undead import CursedUndead
from necromancy_game.warrior import WarriorUndead


class DeathKnight(WarriorUndead, CursedUndead):
    """A fallen knight that combines martial skill with dark curses.

    DeathKnight inherits from both WarriorUndead and CursedUndead, which
    both inherit from Undead (the diamond). Python's MRO is DeathKnight
    -> WarriorUndead -> CursedUndead -> Undead -> object, so Undead is
    only initialised once even though both parents call super().
    """

    SUMMON_NAME = "Death Knight"
    STARTING_HEALTH = 120
    STARTING_POWER = 30
    MIN_HEALTH = 80
    MAX_HEALTH = 300
    MIN_POWER = 20
    MAX_POWER = 90
    HEALTH_PER_LEVEL = 25
    POWER_PER_LEVEL = 7

    def __init__(self, unit_id: int) -> None:
        super().__init__(
            unit_id, self.SUMMON_NAME, self.STARTING_HEALTH,
            self.STARTING_POWER
        )

    def combat_style(self) -> str:
        # super() follows the MRO, so this resolves to WarriorUndead
        # first.
        return f"Death Knight favours: {super().combat_style()}"

    def compare_combat_styles(self) -> str:
        # Explicit class method calls pick a specific parent on purpose,
        # so both styles can be shown side by side.
        warrior_style = WarriorUndead.combat_style(self)
        cursed_style = CursedUndead.combat_style(self)
        return (
            f"Warrior side: {warrior_style}\n"
            f"Cursed side: {cursed_style}"
        )