from abc import ABC, abstractmethod

from banking_system.finance_exceptions import (
    InsufficientFundsError,
    InvalidAmountError,
)
from banking_system.transaction import Transaction


class Account(ABC):
    """The general bank account that every account type is built from.

    Account stores the state shared by all accounts (number, balance
    and transaction history) and provides the common deposit and
    withdraw behaviour. It is abstract because the bank only opens
    specific kinds of account, and each kind must decide what happens
    at the end of the month.
    """

    ACCOUNT_TYPE = "General"
    MINIMUM_AMOUNT = 0
    FIRST_TRANSACTION_ID = 1

    def __init__(self, acc_number: int, opening_balance: float) -> None:
        if isinstance(acc_number, int) and acc_number > 0:
            self.__acc_number = acc_number
        else:
            print("Invalid account number, it must be a positive integer")
            self.__acc_number = 0

        # The balance is protected so subclasses can read it when
        # checking their own rules, but it is still only changed through
        # behaviour.
        if self._is_valid_amount(opening_balance):
            self._balance = opening_balance
        else:
            print("Invalid opening balance, the account will start at $0")
            self._balance = self.MINIMUM_AMOUNT

        self.__transactions = []
        self.__next_transaction_id = self.FIRST_TRANSACTION_ID

    @property
    def acc_number(self) -> int:
        return self.__acc_number

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def transactions(self) -> list:
        # A copy is returned so the history cannot be replaced or edited
        # from outside the account.
        return list(self.__transactions)

    def transaction_count(self) -> int:
        return len(self.__transactions)

    def transactions_of_type(self, transaction_type: str) -> list:
        # A list comprehension filters the history but keeps the order
        # the records were made in.
        return [
            record for record in self.__transactions
            if record.transaction_type == transaction_type
        ]

    def transactions_above(self, amount: float) -> list:
        return [
            record for record in self.__transactions
            if record.amount > amount
        ]

    def statement(self) -> str:
        lines = [f"Statement for {self}"]
        lines += [f"  {record}" for record in self.__transactions]
        if not self.__transactions:
            lines.append("  No transactions yet")
        return "\n".join(lines)

    @abstractmethod
    def month_end(self) -> bool:
        pass

    def deposit(self, amount: float, description: str = "Deposit") -> bool:
        # Rules are checked before the balance changes, so a refused
        # deposit leaves the balance and history untouched.
        if not self._is_valid_amount(amount) or amount == 0:
            raise InvalidAmountError(amount)

        self._balance += amount
        self.__record_transaction("Deposit", amount, description)
        return True

    def withdraw(self, amount: float, description: str = "Withdrawal") -> bool:
        if not self._is_valid_amount(amount) or amount == 0:
            raise InvalidAmountError(amount)

        if amount > self._balance:
            raise InsufficientFundsError(self.__acc_number, amount,
                                         self._balance)

        self._balance -= amount
        self.__record_transaction("Withdrawal", amount, description)
        return True

    def _is_valid_amount(self, amount) -> bool:
        # The bool type is a subclass of int, so it is excluded on
        # purpose.
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
            self._balance,
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
            f"{self.ACCOUNT_TYPE} account {self.__acc_number} "
            f"with a balance of ${self._balance:.2f}"
        )

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(acc_number={self.__acc_number}, "
            f"balance={self._balance}, "
            f"transactions={len(self.__transactions)})"
        )