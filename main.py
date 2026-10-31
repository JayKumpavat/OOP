# from banking_system.account import Account
# from banking_system.branch import Branch
# from banking_system.client import Client
# from banking_system.everyday_account import EverydayAccount
# from banking_system.savings_account import SavingsAccount


# def print_heading(title: str) -> None:
#     print(f"\n=== {title} ===")


# def print_transactions(account: Account) -> None:
#     print(f"Transactions for account {account.acc_number}:")
#     for record in account.transactions:
#         print(f"  {record}")


# # Setup.
# savings = SavingsAccount(1001, 500, 0.025)
# everyday = EverydayAccount(1002, 2000, "4111222233334444")
# client = Client("Alice Smith", 123456789, 412345678)
# adelaide_branch = Branch(1, "Adelaide CBD", "Adelaide", 812345678)
# glenelg_branch = Branch(2, "Glenelg", "Glenelg", 812345679)

# print_heading("Properties (read-only and validated)")
# print(savings.acc_number, savings.balance, savings.interest_rate)
# print(everyday.masked_card_number)
# client.phone_number = 498765432
# print(client.phone_number)
# client.phone_number = 12
# print(client.phone_number)

# print_heading("Client aggregation with different account types")
# client.add_account(savings)
# client.add_account(everyday)
# client.add_account(savings)
# for account in client.accounts:
#     print(account)
# print(f"Total balance: ${client.total_balance():.2f}")

# print_heading("Inherited deposit behaviour")
# savings.deposit(250)
# everyday.deposit(100)
# print(savings)
# print(everyday)

# print_heading("Overridden withdraw behaviour")
# print("Valid savings withdrawal:", savings.withdraw(300))
# print("Savings below minimum:", savings.withdraw(400))
# print("Valid everyday withdrawal:", everyday.withdraw(800))
# print("Everyday above limit:", everyday.withdraw(1500))

# print_heading("Invalid operations create no records")
# print("Negative deposit:", everyday.deposit(-50))
# print("Text withdrawal:", everyday.withdraw("100"))
# savings.apply_interest()
# print_transactions(savings)
# print_transactions(everyday)

# print_heading("isinstance() with the hierarchy")
# print("Savings is an Account:", isinstance(savings, Account))
# print("Everyday is an Account:", isinstance(everyday, Account))
# print("Savings is a SavingsAccount:", isinstance(savings, SavingsAccount))
# print("Savings is an EverydayAccount:", isinstance(savings, EverydayAccount))
# print("Concrete types:", type(savings).__name__, type(everyday).__name__)

# print_heading("Association with a branch")
# client.preferred_branch = adelaide_branch
# client.preferred_branch = "not a branch"
# print(client.preferred_branch)
# client.preferred_branch = glenelg_branch
# glenelg_branch.open_branch()
# glenelg_branch.open_branch()
# glenelg_branch.add_feedback("Friendly staff and short queues.")
# print(client.preferred_branch)
# print(glenelg_branch.feedback)

# print_heading("Removing an account keeps it alive")
# client.remove_account(everyday)
# print(client)
# print(everyday)

from necromancy_game.cursed_undead import CursedUndead
from necromancy_game.death_knight import DeathKnight
from necromancy_game.necromancer import Necromancer
from necromancy_game.phantom_guardian import PhantomGuardian
from necromancy_game.putrid_zombie import PutridZombie
from necromancy_game.skeleton_warrior import SkeletonWarrior
from necromancy_game.summoning_ritual import SummoningRitual
from necromancy_game.undead import Undead
from necromancy_game.vengeful_ghost import VengefulGhost
from necromancy_game.warrior_undead import WarriorUndead


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