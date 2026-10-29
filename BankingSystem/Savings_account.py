from BankingSystem.Accounts import Account

class SavingsAccount(Account):
    """An account that earns interest and keeps a minimum balance."""

    ACCOUNT_TYPE = "Savings"
    MINIMUM_BALANCE = 100
    MAXIMUM_INTEREST_RATE = 0.1

    def __init__(
        self, acc_number: int, opening_balance: float, interest_rate: float
    ) -> None:
        super().__init__(acc_number, opening_balance)

        if (
            isinstance(interest_rate, (int, float))
            and 0 <= interest_rate <= self.MAXIMUM_INTEREST_RATE
        ):
            self.__interest_rate = interest_rate
        else:
            print("Invalid interest rate, it must be between 0 and 0.1")
            self.__interest_rate = 0

    @property
    def interest_rate(self) -> float:
        return self.__interest_rate

    def withdraw(self, amount: float, description: str = "Withdrawal") -> bool:
        # The savings rule is checked first, then the parent finishes
        # the common validation, balance change and transaction record.
        if self._is_valid_amount(amount):
            if self._balance - amount < self.MINIMUM_BALANCE:
                print(
                    f"Withdrawal denied, savings accounts must keep at "
                    f"least ${self.MINIMUM_BALANCE}"
                )
                return False
        return super().withdraw(amount, description)

    def apply_interest(self) -> bool:
        interest = round(self._balance * self.__interest_rate, 2)
        return self.deposit(
            interest, f"Interest at {self.__interest_rate * 100:.1f}%"
        )

    def __str__(self) -> str:
        return (
            f"{super().__str__()} "
            f"(interest rate {self.__interest_rate * 100:.1f}%)"
        )
