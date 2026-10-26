from necromancy_game.necromancer import Necromancer
from necromancy_game.summoning_ritual import SummoningRitual


def print_heading(title: str) -> None:
    print(f"\n=== {title} ===")


# Each ritual leans on the rune that suits its summon: Bone for
# skeletons, Spirit for spectres and Flesh for corpses. Stronger summons
# cost more.
skeleton_ritual = SummoningRitual(
    "Rite of Bones", "Undead Skeleton Warrior", 40, 12,
    bone_cost=4, ectoplasm_cost=1
)
ghost_ritual = SummoningRitual(
    "Wailing Rite", "Vengeful Ghost", 30, 18,
    necrotic_cost=1, spirit_cost=4, ectoplasm_cost=2
)
zombie_ritual = SummoningRitual(
    "Rite of Rot", "Putrid Zombie", 60, 8,
    necrotic_cost=1, flesh_cost=5, ectoplasm_cost=1
)
guardian_ritual = SummoningRitual(
    "Oath of the Phantom", "Phantom Guardian", 70, 10,
    necrotic_cost=2, spirit_cost=4, bone_cost=3, ectoplasm_cost=3
)

morwen = Necromancer("Morwen", necrotic_runes=3, spirit_runes=5,
                     bone_runes=8, flesh_runes=6, ectoplasm=5)
print_heading("Starting necromancer")
print(morwen)

print_heading("Successful summons consume resources")
for ritual in (skeleton_ritual, ghost_ritual, zombie_ritual):
    summoned = morwen.summon(ritual)
    print(f"Summoned: {summoned}")
    print(f"Resources now: {morwen.resource_summary}")

print_heading("A ritual that cannot be performed yet")
print("Summon result:", morwen.summon(guardian_ritual))
print(f"Resources unchanged: {morwen.resource_summary}")
print(f"Army size: {len(morwen.army)}")

print_heading("Collect more resources and try again")
print("Invalid collection:", morwen.collect_resources(spirit_runes=-2))
morwen.collect_resources(necrotic_runes=4, spirit_runes=6, bone_runes=2,
                         ectoplasm=4)
print(f"Resources now: {morwen.resource_summary}")
print(f"Summoned: {morwen.summon(guardian_ritual)}")

print_heading("Levelling through the necromancer")
print("Before:", morwen.describe_undead(1))
morwen.level_undead(1)
print("After: ", morwen.describe_undead(1))
print("Level a missing id:", morwen.level_undead(99))

print_heading("Dismissing an undead")
print("Dismiss #2:", morwen.dismiss(2))
print("Dismiss #2 again:", morwen.dismiss(2))

print_heading("Final necromancer")
print(morwen)
