from banking_system.account import Account

class EverydayAccount(Account):
    """A transaction account with a linked debit card and a limit on
    each single withdrawal.
    """

    ACCOUNT_TYPE = "Everyday"
    MAXIMUM_WITHDRAWAL = 1000
    MONTHLY_FEE = 5
    FEE_FREE_BALANCE = 2000
    CARD_NUMBER_LENGTH = 16

    def __init__(
        self, acc_number: int, opening_balance: float, card_number: str
    ) -> None:
        super().__init__(acc_number, opening_balance)

        if (
            isinstance(card_number, str)
            and card_number.isdigit()
            and len(card_number) == self.CARD_NUMBER_LENGTH
        ):
            self.__card_number = card_number
        else:
            print("Invalid card number, the account has no linked card")
            self.__card_number = None

    @property
    def masked_card_number(self) -> str:
        # Only the last four digits are ever shown outside the account.
        if self.__card_number is None:
            return "No card linked"
        return "**** **** **** " + self.__card_number[-4:]

    def withdraw(self, amount: float, description: str = "Withdrawal") -> bool:
        if self._is_valid_amount(amount) and amount > self.MAXIMUM_WITHDRAWAL:
            print(
                f"Withdrawal denied, everyday accounts can only withdraw "
                f"up to ${self.MAXIMUM_WITHDRAWAL} at a time"
            )
            return False
        return super().withdraw(amount, description)

    def month_end(self) -> bool:
        # Everyday accounts pay a small fee unless the balance is high
        # enough to have it waived.
        if self._balance >= self.FEE_FREE_BALANCE:
            return False
        return self.withdraw(self.MONTHLY_FEE, "Monthly account fee")

    def __str__(self) -> str:
        return f"{super().__str__()} (card {self.masked_card_number})"