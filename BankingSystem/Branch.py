class Branch:
    """A physical bank branch that clients can choose as their preferred
    branch.
    """

    PHONE_NUMBER_LENGTH = 9

    def __init__(
        self,
        branch_number: int,
        branch_name: str,
        branch_suburb: str,
        branch_phone_number: int,
    ) -> None:
        if isinstance(branch_number, int) and branch_number > 0:
            self.__branch_number = branch_number
        else:
            print("Invalid branch number, it must be a positive integer")
            self.__branch_number = 0

        self.__branch_name = "Unnamed branch"
        self.__branch_suburb = "Unknown suburb"
        self.__phone_number = None
        self.__status = "Closed"
        self.__feedback = []

        # The setters are reused so the constructor applies the same
        # validation as later updates.
        self.branch_name = branch_name
        self.branch_suburb = branch_suburb
        self.phone_number = branch_phone_number

    @property
    def branch_number(self) -> int:
        return self.__branch_number

    @property
    def branch_name(self) -> str:
        return self.__branch_name

    @branch_name.setter
    def branch_name(self, new_name: str) -> None:
        if isinstance(new_name, str) and new_name.strip() != "":
            self.__branch_name = new_name
        else:
            print("Invalid branch name, it must be a non-empty string")

    @property
    def branch_suburb(self) -> str:
        return self.__branch_suburb

    @branch_suburb.setter
    def branch_suburb(self, new_suburb: str) -> None:
        if isinstance(new_suburb, str) and new_suburb.strip() != "":
            self.__branch_suburb = new_suburb
        else:
            print("Invalid suburb, it must be a non-empty string")

    @property
    def phone_number(self) -> int:
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, new_number: int) -> None:
        if (
            isinstance(new_number, int)
            and len(str(new_number)) == self.PHONE_NUMBER_LENGTH
        ):
            self.__phone_number = new_number
        else:
            print("Invalid phone number, it must be 9 digits without the 0")

    @property
    def status(self) -> str:
        return self.__status

    @property
    def feedback(self) -> list:
        return list(self.__feedback)

    def open_branch(self) -> bool:
        if self.__status == "Open":
            print(f"{self.__branch_name} is already open")
            return False
        self.__status = "Open"
        return True

    def close_branch(self) -> bool:
        if self.__status == "Closed":
            print(f"{self.__branch_name} is already closed")
            return False
        self.__status = "Closed"
        return True

    def add_feedback(self, comment: str) -> bool:
        if not isinstance(comment, str) or comment.strip() == "":
            print("Feedback must be a non-empty string")
            return False
        self.__feedback.append(comment)
        return True

    def __eq__(self, other) -> bool:
        if not isinstance(other, Branch):
            return False
        return self.__branch_number == other.branch_number

    def __str__(self) -> str:
        return (
            f"Branch {self.__branch_number} - {self.__branch_name}, "
            f"{self.__branch_suburb} (phone 0{self.__phone_number}, "
            f"{self.__status})"
        )

    def __repr__(self) -> str:
        return (
            f"Branch({self.__branch_number}, '{self.__branch_name}', "
            f"'{self.__branch_suburb}', {self.__phone_number})"
        )
