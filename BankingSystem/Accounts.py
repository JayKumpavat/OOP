from banking_system.transaction import Transaction


class Account:
    """A bank account that stores its balance and creates a record for
    every successful deposit and withdrawal (composition).
    """

    MINIMUM_AMOUNT = 0
    FIRST_TRANSACTION_ID = 1

    def __init__(
        self, acc_number: int, acc_type: str, opening_balance: float
    ) -> None:
        if isinstance(acc_number, int) and acc_number > 0:
            self.__acc_number = acc_number
        else:
            print("Invalid account number, it must be a positive integer")
            self.__acc_number = 0

        self.__acc_type = "General"
        self.acc_type = acc_type

        if self.__is_valid_amount(opening_balance):
            self.__balance = opening_balance
        else:
            print("Invalid opening balance, the account will start at $0")
            self.__balance = self.MINIMUM_AMOUNT

        self.__transactions = []
        self.__next_transaction_id = self.FIRST_TRANSACTION_ID

    @property
    def acc_number(self) -> int:
        return self.__acc_number

    @property
    def acc_type(self) -> str:
        return self.__acc_type

    @acc_type.setter
    def acc_type(self, new_type: str) -> None:
        if isinstance(new_type, str) and new_type.strip() != "":
            self.__acc_type = new_type
        else:
            print("Invalid account type, it must be a non-empty string")

    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def transactions(self) -> list:
        # A copy is returned so the history cannot be replaced or edited
        # from outside the account.
        return list(self.__transactions)

    def deposit(self, amount: float, description: str = "Deposit") -> bool:
        if not self.__is_valid_amount(amount) or amount == 0:
            print("Deposit denied, the amount must be a positive number")
            return False

        self.__balance += amount
        self.__record_transaction("Deposit", amount, description)
        return True

    def withdraw(self, amount: float, description: str = "Withdrawal") -> bool:
        if not self.__is_valid_amount(amount) or amount == 0:
            print("Withdrawal denied, the amount must be a positive number")
            return False

        if amount > self.__balance:
            print("Withdrawal denied, insufficient balance")
            return False

        self.__balance -= amount
        self.__record_transaction("Withdrawal", amount, description)
        return True

    def __is_valid_amount(self, amount) -> bool:
        # bool is a subclass of int, so it is excluded on purpose.
        return (
            isinstance(amount, (int, float))
            and not isinstance(amount, bool)
            and amount >= self.MINIMUM_AMOUNT
        )

    def __record_transaction(
        self, transaction_type: str, amount: float, description: str
    ) -> None:
        # Only called after a successful balance change, so failed
        # operations never create a record.
        record = Transaction(
            self.__next_transaction_id,
            transaction_type,
            amount,
            self.__balance,
            description,
        )
        self.__transactions.append(record)
        self.__next_transaction_id += 1

    def __eq__(self, other) -> bool:
        # Account numbers are unique, so they identify an account.
        if not isinstance(other, Account):
            return False
        return self.__acc_number == other.acc_number

    def __str__(self) -> str:
        return (
            f"{self.__acc_type} account {self.__acc_number} "
            f"with a balance of ${self.__balance:.2f}"
        )

    def __repr__(self) -> str:
        return (
            f"Account(acc_number={self.__acc_number}, "
            f"acc_type='{self.__acc_type}', balance={self.__balance}, "
            f"transactions={len(self.__transactions)})"
        )