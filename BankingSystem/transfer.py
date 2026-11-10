from banking_system.account import Account


class Transfer:
    """Moves money between two accounts.

    Transfer never changes a balance itself. It asks the source account
    to withdraw and the destination account to deposit, so each account
    keeps applying its own rules and recording its own transactions.
    """

    def __init__(
        self, source: Account, destination: Account, amount: float
    ) -> None:
        self.__source = source
        self.__destination = destination
        self.__amount = amount
        self.__status = "Pending"

    def execute(self) -> bool:
        if self.__status != "Pending":
            print(f"This transfer has already been {self.__status.lower()}")
            return False

        if not (
            isinstance(self.__source, Account)
            and isinstance(self.__destination, Account)
        ):
            print("Transfer failed, both sides must be Account objects")
            self.__status = "Failed"
            return False

        if self.__source == self.__destination:
            print("Transfer failed, cannot transfer to the same account")
            self.__status = "Failed"
            return False

        withdrawn = self.__source.withdraw(
            self.__amount, f"Transfer to {self.__destination.acc_number}"
        )
        if not withdrawn:
            self.__status = "Failed"
            return False

        self.__destination.deposit(
            self.__amount, f"Transfer from {self.__source.acc_number}"
        )
        self.__status = "Completed"
        return True

    def __str__(self) -> str:
        return (
            f"Transfer of ${self.__amount:.2f} from "
            f"{self.__source.acc_number} to "
            f"{self.__destination.acc_number}: {self.__status}"
        )