"""Shared fixtures for the gym tracker test suite.

Each fixture only builds a known starting state. The behaviour being
tested always happens inside the test itself.
"""
import pytest

from gym_tracker.cardio_exercise import CardioExercise
from gym_tracker.gym import Gym
from gym_tracker.member import Member
from gym_tracker.mobility_exercise import MobilityExercise
from gym_tracker.strength_exercise import StrengthExercise
from gym_tracker.trainer import Trainer


@pytest.fixture
def bench_press():
    return StrengthExercise("Bench Press", 4, 8, 60,
                            ["chest", "arms", "shoulders"])


@pytest.fixture
def squat():
    return StrengthExercise("Back Squat", 5, 5, 80, ["legs", "glutes"])


@pytest.fixture
def treadmill():
    return CardioExercise("Treadmill Run", 1, 20, 2, ["legs"])


@pytest.fixture
def stretch():
    return MobilityExercise("Hamstring Stretch", 3, 30, ["legs"])


@pytest.fixture
def member():
    return Member("Jay", 101, "Build strength")


@pytest.fixture
def trainer():
    return Trainer("Lee", 201, "Powerlifting")


@pytest.fixture
def full_trainer():
    trainer = Trainer("Ava", 202, "Endurance")
    for _ in range(Trainer.MAX_CLIENTS):
        trainer.take_on_client()
    return trainer


@pytest.fixture
def workout(member):
    return member.start_workout("Push Day", "2026-10-20")


@pytest.fixture
def full_workout(workout, bench_press, treadmill, stretch):
    # A workout that already holds one of each exercise type.
    workout.add_exercise(bench_press)
    workout.add_exercise(treadmill)
    workout.add_exercise(stretch)
    return workout


@pytest.fixture
def gym(member, trainer):
    gym = Gym("Northside Strength Club")
    gym.register_member(member)
    gym.register_member(Member("Sam", 102, "Improve fitness"))
    gym.register_trainer(trainer)
    return gym


@pytest.fixture
def rower():
    return CardioExercise("Rowing Intervals", 4, 3, 3,
                          ["back", "legs", "arms"])


@pytest.fixture
def quad_stretch():
    return MobilityExercise("Quad Stretch", 2, 45, ["legs"])


@pytest.fixture
def coached_member(member, trainer):
    member.assign_trainer(trainer)
    return member


@pytest.fixture
def empty_gym():
    return Gym("Empty Gym")