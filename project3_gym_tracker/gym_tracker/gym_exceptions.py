"""Custom exceptions for rules that are specific to the gym tracker."""


class GymError(Exception):
    """Parent for every gym-specific problem, so callers can catch the
    whole family at once.
    """


class MemberNotFoundError(GymError):
    """Raised when the gym is asked for a member id it does not have."""

    def __init__(self, member_id: int) -> None:
        # The id is kept so the caller can report which member was
        # missing.
        self.member_id = member_id
        super().__init__(f"No member with id {member_id} is registered")


class TrainerNotFoundError(GymError):
    """Raised when the gym has no trainer with the requested id."""

    def __init__(self, trainer_id: int) -> None:
        # The id is kept so the caller can report which trainer was
        # missing.
        self.trainer_id = trainer_id
        super().__init__(f"No trainer with id {trainer_id} is registered")


class TrainerFullError(GymError):
    """Raised when a trainer already has the most members allowed."""

    def __init__(self, trainer_name: str, max_clients: int) -> None:
        # The limit is stored so the message and the caller both show
        # the same maximum the trainer is held to.
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
    """Raised when a finished workout is changed or completed again."""

    def __init__(self, workout_title: str) -> None:
        # A completed workout is a record of the session, so it is
        # locked against any further changes.
        super().__init__(workout_title,
                         "the workout is finished and cannot change")


class EmptyWorkoutError(WorkoutError):
    """Raised when a workout with no exercises is marked as complete."""

    def __init__(self, workout_title: str) -> None:
        # An empty workout has nothing to log, so it cannot be
        # completed.
        super().__init__(workout_title,
                         "a workout needs at least one exercise")


class DuplicateExerciseError(WorkoutError):
    """Raised when the same exercise is added to a workout twice."""

    def __init__(self, workout_title: str, exercise_name: str) -> None:
        # The exercise name is kept so the caller knows which one was
        # repeated.
        self.exercise_name = exercise_name
        super().__init__(workout_title,
                         f"{exercise_name} is already in this workout")


class WorkoutFullError(WorkoutError):
    """Raised when a workout already has the most exercises allowed."""

    def __init__(self, workout_title: str, max_exercises: int) -> None:
        # The limit is stored so the message matches the workout's
        # MAX_EXERCISES constant.
        self.max_exercises = max_exercises
        super().__init__(workout_title,
                         f"a workout can hold at most {max_exercises} "
                         f"exercises")
