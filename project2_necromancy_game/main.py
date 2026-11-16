from necromancy_game.cursed_undead import CursedUndead
from necromancy_game.death_knight import DeathKnight
from necromancy_game.necromancer import Necromancer
from necromancy_game.phantom_gaurdian import PhantomGuardian
from necromancy_game.putrid_zombie import PutridZombie
from necromancy_game.skeleton_warrior import SkeletonWarrior
from necromancy_game.summoning_ritual import SummoningRitual
from necromancy_game.undead import Undead
from necromancy_game.vengeful_ghost import VengefulGhost
from necromancy_game.warrior import WarriorUndead


def print_heading(title: str) -> None:
    print(f"\n=== {title} ===")


# Each ritual leans on the rune that suits its summon: Bone for
# skeletons, Spirit for spectres and Flesh for corpses.
skeleton_ritual = SummoningRitual(
    "Rite of Bones", SkeletonWarrior, bone_cost=4, ectoplasm_cost=1
)
ghost_ritual = SummoningRitual(
    "Wailing Rite", VengefulGhost, necrotic_cost=1, spirit_cost=4,
    ectoplasm_cost=2
)
zombie_ritual = SummoningRitual(
    "Rite of Rot", PutridZombie, necrotic_cost=1, flesh_cost=5,
    ectoplasm_cost=1
)
guardian_ritual = SummoningRitual(
    "Oath of the Phantom", PhantomGuardian, necrotic_cost=2,
    spirit_cost=4, bone_cost=3, ectoplasm_cost=3
)
death_knight_ritual = SummoningRitual(
    "Rite of the Fallen Knight", DeathKnight, necrotic_cost=5,
    spirit_cost=5, bone_cost=5, flesh_cost=5, ectoplasm_cost=6
)
broken_ritual = SummoningRitual("Rite Without Ectoplasm", SkeletonWarrior,
                                bone_cost=1, ectoplasm_cost=0)

print_heading("Rituals")
for ritual in (skeleton_ritual, ghost_ritual, zombie_ritual,
               guardian_ritual, death_knight_ritual, broken_ritual):
    print(ritual)

morwen = Necromancer("Morwen", necrotic_runes=6, spirit_runes=8,
                     bone_runes=10, flesh_runes=6, ectoplasm=8)
print_heading("Starting necromancer")
print(morwen)

print_heading("Successful summons consume resources")
for ritual in (skeleton_ritual, ghost_ritual, zombie_ritual):
    summoned = morwen.summon(ritual)
    print(f"Summoned: {summoned}")
    print(f"Resources now: {morwen.resource_summary}")

print_heading("A ritual that cannot be performed yet")
print("Summon result:", morwen.summon(death_knight_ritual))
print(f"Resources unchanged: {morwen.resource_summary}")
print(f"Army size: {len(morwen.army)}")

print_heading("Collect more resources and try again")
print("Invalid collection:", morwen.collect_resources(bone_runes=-5))
morwen.collect_resources(necrotic_runes=10, spirit_runes=10, bone_runes=5,
                         flesh_runes=5, ectoplasm=10)
print(f"Resources now: {morwen.resource_summary}")
death_knight = morwen.summon(death_knight_ritual)
print(f"Summoned: {death_knight}")

print_heading("Inheritance checks")
for undead in morwen.army:
    print(
        f"{undead.name}: Undead={isinstance(undead, Undead)}, "
        f"Warrior={isinstance(undead, WarriorUndead)}, "
        f"Cursed={isinstance(undead, CursedUndead)}, "
        f"type={type(undead).__name__}"
    )

print_heading("Death Knight MRO")
print(" -> ".join(cls.__name__ for cls in DeathKnight.mro()))

print_heading("Ambiguous combat_style() resolved by super()")
print(death_knight.combat_style())

print_heading("Explicit parent class method calls")
print(death_knight.compare_combat_styles())

print_heading("Overridden command() across the army")
for order in morwen.command_army():
    print(order)
print(f"Death Knight battles fought: {death_knight.battles_fought}, "
      f"curses cast: {death_knight.curses_cast}")

print_heading("Levelling through the necromancer")
print("Before:", morwen.describe_undead(death_knight.unit_id))
morwen.level_undead(death_knight.unit_id)
print("After: ", morwen.describe_undead(death_knight.unit_id))
print("Before:", morwen.describe_undead(1))
for attempt in range(12):
    morwen.level_undead(1)
print("After: ", morwen.describe_undead(1))

print_heading("Dismissing an undead")
print("Dismiss #2:", morwen.dismiss(2))
print("Dismiss #2 again:", morwen.dismiss(2))
print(morwen.command_undead(2))

print_heading("Final necromancer")
morwen.summon(guardian_ritual)
print(morwen)
