class Transaction:
    """A record of one successful deposit or withdrawal on an account.

    Transaction objects are created and owned by an Account
    (composition). Once a record is created it cannot be changed, so
    every attribute is private. Only the type and amount have read-only
    properties, because the account filters its history by them.
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
    def transaction_type(self) -> str:
        return self.__transaction_type

    @property
    def amount(self) -> float:
        return self.__amount

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
