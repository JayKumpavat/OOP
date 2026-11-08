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

from gym_tracker.cardio_exercise import CardioExercise
from gym_tracker.exercise import Exercise
from gym_tracker.gym import Gym
from gym_tracker.member import Member
from gym_tracker.mobility_exercise import MobilityExercise
from gym_tracker.progressable import Progressable
from gym_tracker.strength_exercise import StrengthExercise
from gym_tracker.trainer import Trainer


def print_heading(title: str) -> None:
    print(f"\n=== {title} ===")


# Exercises exist independently so they can be reused across workouts.
bench_press = StrengthExercise("Bench Press", 4, 8, 60,
                               ["chest", "arms", "shoulders"])
squat = StrengthExercise("Back Squat", 5, 5, 80, ["legs", "glutes", "core"])
deadlift = StrengthExercise("Deadlift", 3, 5, 100,
                            ["back", "legs", "glutes"])
treadmill = CardioExercise("Treadmill Run", 1, 20, 2, ["legs"])
rower = CardioExercise("Rowing Intervals", 4, 3, 3, ["back", "legs", "arms"])
hamstring_stretch = MobilityExercise("Hamstring Stretch", 3, 30, ["legs"])

jay = Member("Jay", 101, "Build strength")
sam = Member("Sam", 102, "Improve fitness")
mia = Member("Mia", 103, "Run a half marathon")
coach_lee = Trainer("Lee", 201, "Powerlifting")
coach_ava = Trainer("Ava", 202, "Endurance")

print_heading("Abstract classes cannot be created directly")
print("Abstract methods on Exercise:",
      sorted(Exercise.__abstractmethods__))
print("StrengthExercise is an Exercise:",
      isinstance(bench_press, Exercise))
print("StrengthExercise is Progressable:",
      isinstance(bench_press, Progressable))
print("MobilityExercise is Progressable:",
      isinstance(hamstring_stretch, Progressable))

print_heading("Validation")
bad_lift = StrengthExercise("Bad Lift", 20, 50, -10, ["chest", "wings"])
print(bad_lift)

print_heading("Dictionary: registering people with the gym")
gym = Gym("Northside Strength Club")
for member in (jay, sam, mia):
    gym.register_member(member)
gym.register_member(Member("Jay Copy", 101, "Duplicate id"))
gym.register_trainer(coach_lee)
gym.register_trainer(coach_ava)
print(gym)
print("Member ids:", sorted(gym.members))
print("Is 102 a member?", gym.is_member(102))
print("Is 999 a member?", gym.is_member(999))
print("Look up 103:", gym.find_member(103))

print_heading("Dictionary: assigning trainers by id")
gym.assign_trainer(101, 201)
gym.assign_trainer(102, 202)
gym.assign_trainer(103, 202)
gym.assign_trainer(999, 201)
for person in (coach_lee, coach_ava):
    print(person)
coached = gym.members_coached_by(202)
print("Coached by Ava:", [member.name for member in coached])

print_heading("Composition: members create their own workouts")
push_day = jay.start_workout("Push Day", "2026-10-20")
push_day.add_exercise(bench_press)
push_day.add_exercise(treadmill)
push_day.add_exercise(hamstring_stretch)
push_day.add_exercise(StrengthExercise("bench press", 3, 10, 50))
push_day.add_exercise("not an exercise")
print(push_day)

print_heading("Polymorphic calories across different exercise types")
for exercise in push_day.exercises:
    print(f"{type(exercise).__name__:<17}"
          f"{exercise.calculate_calories():>7.1f} kcal")
push_day.complete()
print("After Push Day Jay still needs:", sorted(jay.untrained_muscles()))

print_heading("Progressive overload through the interface")
leg_day = jay.start_workout("Leg Day", "2026-10-22")
leg_day.add_exercise(squat)
leg_day.add_exercise(rower)
leg_day.add_exercise(hamstring_stretch)
for result in leg_day.progress_exercises():
    print(result)
leg_day.complete()

print_heading("Set: muscle groups")
print("Bench press targets chest?", bench_press.targets("chest"))
print("Push Day muscles:", sorted(push_day.muscles_trained()))
print("Leg Day muscles: ", sorted(leg_day.muscles_trained()))
print("Worked in both:  ", sorted(push_day.shared_muscles(leg_day)))
print(f"Jay has logged {len(jay.workouts)} workouts")
print("Jay has trained: ", sorted(jay.muscles_trained()))
print("Jay still needs: ", sorted(jay.untrained_muscles()) or "nothing")

run_day = mia.start_workout("Long Run", "2026-10-23")
run_day.add_exercise(treadmill)
run_day.add_exercise(deadlift)
run_day.complete()

print_heading("Dictionary: calories by member")
for name, calories in gym.calories_by_member().items():
    print(f"{name:<5}{calories:>8.1f} kcal")

print_heading("Removing a member frees their trainer's spot")
print(f"Ava coaches {coach_ava.client_count} member(s)")
gym.remove_member(103)
gym.remove_member(103)
print(f"Ava now coaches {coach_ava.client_count} member(s)")
print(gym)