class Transaction:
    """A record of one successful deposit or withdrawal on an account.

    Transaction objects are created and owned by an Account
    (composition). Once a record is created it cannot be changed, so
    every attribute is private and exposed through read-only properties.
    """

    def __init__(
        self,
        transaction_id: int,
        transaction_type: str,
        amount: float,
        resulting_balance: float,
        description: str,
    ) -> None:
        self.__transaction_id = transaction_id
        self.__transaction_type = transaction_type
        self.__amount = amount
        self.__resulting_balance = resulting_balance
        self.__description = description

    @property
    def transaction_id(self) -> int:
        return self.__transaction_id

    @property
    def transaction_type(self) -> str:
        return self.__transaction_type

    @property
    def amount(self) -> float:
        return self.__amount

    @property
    def resulting_balance(self) -> float:
        return self.__resulting_balance

    @property
    def description(self) -> str:
        return self.__description

    def __eq__(self, other) -> bool:
        # Two records are the same if every stored value matches.
        if not isinstance(other, Transaction):
            return False
        return (
            self.__transaction_id == other.transaction_id
            and self.__transaction_type == other.transaction_type
            and self.__amount == other.amount
            and self.__resulting_balance == other.resulting_balance
        )

    def __str__(self) -> str:
        return (
            f"#{self.__transaction_id} {self.__transaction_type} of "
            f"${self.__amount:.2f} ({self.__description}), "
            f"balance after: ${self.__resulting_balance:.2f}"
        )

    def __repr__(self) -> str:
        return (
            f"Transaction({self.__transaction_id}, "
            f"'{self.__transaction_type}', {self.__amount}, "
            f"{self.__resulting_balance}, '{self.__description}')"
        )
