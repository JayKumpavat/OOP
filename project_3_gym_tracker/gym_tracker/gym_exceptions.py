"""Custom exceptions for rules that are specific to the gym tracker."""


class GymError(Exception):
    """Parent for every gym-specific problem, so callers can catch the
    whole family at once.
    """


class MemberNotFoundError(GymError):
    def __init__(self, member_id: int) -> None:
        self.member_id = member_id
        super().__init__(f"No member with id {member_id} is registered")


class TrainerNotFoundError(GymError):
    def __init__(self, trainer_id: int) -> None:
        self.trainer_id = trainer_id
        super().__init__(f"No trainer with id {trainer_id} is registered")


class TrainerFullError(GymError):
    def __init__(self, trainer_name: str, max_clients: int) -> None:
        self.trainer_name = trainer_name
        self.max_clients = max_clients
        super().__init__(
            f"{trainer_name} already coaches the maximum of "
            f"{max_clients} members"
        )


class WorkoutError(GymError):
    """Parent for problems with changing a workout."""

    def __init__(self, workout_title: str, message: str) -> None:
        self.workout_title = workout_title
        super().__init__(f"{workout_title}: {message}")


class WorkoutCompletedError(WorkoutError):
    def __init__(self, workout_title: str) -> None:
        super().__init__(workout_title,
                         "the workout is finished and cannot change")


class EmptyWorkoutError(WorkoutError):
    def __init__(self, workout_title: str) -> None:
        super().__init__(workout_title,
                         "a workout needs at least one exercise")


class DuplicateExerciseError(WorkoutError):
    def __init__(self, workout_title: str, exercise_name: str) -> None:
        self.exercise_name = exercise_name
        super().__init__(workout_title,
                         f"{exercise_name} is already in this workout")


class WorkoutFullError(WorkoutError):
    def __init__(self, workout_title: str, max_exercises: int) -> None:
        self.max_exercises = max_exercises
        super().__init__(workout_title,
                         f"a workout can hold at most {max_exercises} "
                         f"exercises")