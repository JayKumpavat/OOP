from NecromancerGame.resource_pool import ResourcePool
from NecromancerGame.summoning_ritual import SummoningRitual


def print_heading(title: str) -> None:
    print(f"\n--- {title} ---")


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
rituals = [skeleton_ritual, ghost_ritual, zombie_ritual, guardian_ritual]

print_heading("Rituals")
for ritual in rituals:
    print(ritual)

print_heading("Ritual without Ectoplasm is corrected")
broken_ritual = SummoningRitual(
    "Rite Without Ectoplasm", "Undead Skeleton Warrior", 40, 12,
    bone_cost=1, ectoplasm_cost=0
)
print(broken_ritual)

resources = ResourcePool(necrotic_runes=2, spirit_runes=3, bone_runes=10,
                         flesh_runes=6, ectoplasm=5)
print_heading("Starting resources")
print(resources)

print_heading("Which rituals can be performed")
for ritual in rituals:
    print(f"{ritual.ritual_name}: {ritual.can_perform(resources)}")
print("Invalid pool:", skeleton_ritual.can_perform("not a pool"))

print_heading("Invalid collection leaves resources unchanged")
print("Collect -3 bone runes:", resources.collect(bone_runes=-3))
print("Collect 2.5 spirit runes:", resources.collect(spirit_runes=2.5))
print(resources)

print_heading("Failed spend leaves resources unchanged")
print("Perform Phantom Guardian:",
      guardian_ritual.consume_resources(resources))
print(resources)

print_heading("Performing a ritual and creating an undead")
if skeleton_ritual.consume_resources(resources):
    skeleton = skeleton_ritual.create_summon(1)
    print(f"Created: {skeleton}")
print(f"Resources after: {resources}")

print_heading("Levelling the undead")
print(f"Before: {skeleton}")
skeleton.level_up()
print(f"After:  {skeleton}")

print_heading("Levelling stops at the maximum level")
for attempt in range(10):
    skeleton.level_up()
print(skeleton)

