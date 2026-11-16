from gym_tracker.exercise import Exercise
from gym_tracker.gym_exceptions import WorkoutError
from gym_tracker.person import Person
from gym_tracker.trainer import Trainer
from gym_tracker.workout import Workout


class Member(Person):
    """A gym member who logs workouts and can be coached by a trainer.

    The member creates and owns their workouts (composition) and holds a
    reference to at most one trainer (association).
    """

    def __init__(self, name: str, person_id: int, goal: str) -> None:
        super().__init__(name, person_id)
        self.__goal = goal
        self.__workouts = []
        self.__trainer = None

    @property
    def workouts(self) -> list:
        return list(self.__workouts)

    @property
    def trainer(self) -> Trainer:
        return self.__trainer

    def start_workout(self, title: str, date: str) -> Workout:
        workout = Workout(title, date)
        self.__workouts.append(workout)
        return workout

    def assign_trainer(self, trainer: Trainer) -> bool:
        if not isinstance(trainer, Trainer):
            print("Only a Trainer can be assigned")
            return False
        if trainer == self.__trainer:
            print(f"{trainer.name} already coaches {self.name}")
            return False
        # Calling take_on_client() raises TrainerFullError before
        # anything is linked, so a full trainer leaves the member
        # unchanged.
        trainer.take_on_client()
        # The old trainer frees up a spot before the new one is linked.
        if self.__trainer is not None:
            self.__trainer.release_client()
        self.__trainer = trainer
        return True

    def add_to_workout(self, workout: Workout, exercise: Exercise) -> bool:
        if workout not in self.__workouts:
            print(f"{self.name} does not own that workout")
            return False
        try:
            return workout.add_exercise(exercise)
        except WorkoutError as error:
            print(f"Could not add exercise. {error}")
            return False

    def finish_workout(self, workout: Workout) -> bool:
        if workout not in self.__workouts:
            print(f"{self.name} does not own that workout")
            return False
        try:
            return workout.complete()
        except WorkoutError as error:
            print(f"Could not finish workout. {error}")
            return False

    def remove_trainer(self) -> bool:
        if self.__trainer is None:
            return False
        self.__trainer.release_client()
        self.__trainer = None
        return True

    def muscles_trained(self) -> set:
        trained = set()
        for workout in self.__workouts:
            if workout.completed:
                trained |= workout.muscles_trained()
        return trained

    def untrained_muscles(self) -> set:
        # Difference between every muscle group and the ones already
        # trained shows what to plan for next.
        return Exercise.MUSCLE_GROUPS - self.muscles_trained()

    def total_calories(self) -> float:
        total = 0
        for workout in self.__workouts:
            if workout.completed:
                total += workout.total_calories()
        return total

    def completed_workout_count(self) -> int:
        count = 0
        for workout in self.__workouts:
            if workout.completed:
                count += 1
        return count

    def role_summary(self) -> str:
        coach = self.__trainer.name if self.__trainer else "no trainer"
        return (
            f"Member, goal: {self.__goal}, coached by {coach}, "
            f"{self.completed_workout_count()} workout(s) done"
        )