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
jay.add_to_workout(push_day, bench_press)
jay.add_to_workout(push_day, treadmill)
jay.add_to_workout(push_day, hamstring_stretch)
jay.add_to_workout(push_day, StrengthExercise("bench press", 3, 10, 50))
jay.add_to_workout(push_day, "not an exercise")
print(push_day)

print_heading("Polymorphic calories across different exercise types")
for exercise in push_day.exercises:
    print(f"{type(exercise).__name__:<17}"
          f"{exercise.calculate_calories():>7.1f} kcal")
jay.finish_workout(push_day)
print("After Push Day Jay still needs:", sorted(jay.untrained_muscles()))

print_heading("Progressive overload through the interface")
leg_day = jay.start_workout("Leg Day", "2026-10-22")
jay.add_to_workout(leg_day, squat)
jay.add_to_workout(leg_day, rower)
jay.add_to_workout(leg_day, hamstring_stretch)
for result in leg_day.progress_exercises():
    print(result)
jay.finish_workout(leg_day)

print_heading("Set: muscle groups")
print("Bench press targets chest?", bench_press.targets("chest"))
print("Push Day muscles:", sorted(push_day.muscles_trained()))
print("Leg Day muscles: ", sorted(leg_day.muscles_trained()))
print("Worked in both:  ", sorted(push_day.shared_muscles(leg_day)))
print(f"Jay has logged {len(jay.workouts)} workouts")
print("Jay has trained: ", sorted(jay.muscles_trained()))
print("Jay still needs: ", sorted(jay.untrained_muscles()) or "nothing")

run_day = mia.start_workout("Long Run", "2026-10-23")
mia.add_to_workout(run_day, treadmill)
mia.add_to_workout(run_day, deadlift)
mia.finish_workout(run_day)

print_heading("Dictionary: calories by member")
for name, calories in gym.calories_by_member().items():
    print(f"{name:<5}{calories:>8.1f} kcal")

print_heading("Handled exceptions: the program carries on")
rest_day = sam.start_workout("Rest Day", "2026-10-24")
sam.finish_workout(rest_day)
jay.add_to_workout(push_day, squat)
jay.finish_workout(push_day)
jay.add_to_workout(rest_day, squat)
for member_id in range(104, 109):
    gym.register_member(Member(f"Guest {member_id}", member_id, "Trial"))
    gym.assign_trainer(member_id, 201)
print(coach_lee)
gym.assign_trainer(102, 999)
gym.members_coached_by(999)
print("Push Day is unchanged:", [e.name for e in push_day.exercises])
print("Sam's trainer is still:", sam.trainer.name)

print_heading("Removing a member frees their trainer's spot")
print(f"Ava coaches {coach_ava.client_count} member(s)")
gym.remove_member(103)
gym.remove_member(103)
print(f"Ava now coaches {coach_ava.client_count} member(s)")
print(gym)