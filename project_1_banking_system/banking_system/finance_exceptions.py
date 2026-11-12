"""Custom exceptions for rules that are specific to Finance."""


class FinanceError(Exception):
    """Parent for every Finance problem, so a caller can catch the whole
    family with one except clause.
    """


class InvalidAmountError(FinanceError):
    """A deposit or withdrawal amount was not a positive number."""

    def __init__(self, amount) -> None:
        self.amount = amount
        super().__init__(
            f"{amount!r} is not a valid amount, it must be a positive number"
        )


class WithdrawalError(FinanceError):
    """Parent for every reason a withdrawal can be refused."""

    def __init__(self, acc_number: int, amount: float, reason: str) -> None:
        self.acc_number = acc_number
        self.amount = amount
        super().__init__(
            f"Account {acc_number} cannot withdraw ${amount:.2f}: {reason}"
        )


class InsufficientFundsError(WithdrawalError):
    """A withdrawal is larger than the account balance."""

    def __init__(self, acc_number: int, amount: float,
                 balance: float) -> None:
        self.balance = balance
        super().__init__(acc_number, amount,
                         f"the balance is only ${balance:.2f}")


class MinimumBalanceError(WithdrawalError):
    """A savings withdrawal would go below the minimum balance."""

    def __init__(self, acc_number: int, amount: float, balance: float,
                 minimum: float) -> None:
        self.balance = balance
        self.minimum = minimum
        super().__init__(
            acc_number, amount,
            f"savings must keep at least ${minimum:.2f} and the balance "
            f"is ${balance:.2f}"
        )


class WithdrawalLimitError(WithdrawalError):
    """An everyday withdrawal is over the single withdrawal limit."""

    def __init__(self, acc_number: int, amount: float,
                 limit: float) -> None:
        self.limit = limit
        super().__init__(acc_number, amount,
                         f"the limit for one withdrawal is ${limit:.2f}")


class AccountNotFoundError(FinanceError):
    """A client was asked for an account number they do not hold."""

    def __init__(self, client_id: int, acc_number: int) -> None:
        self.client_id = client_id
        self.acc_number = acc_number
        super().__init__(
            f"Client {client_id} does not hold account {acc_number}"
        )