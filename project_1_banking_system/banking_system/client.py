from banking_system.account import Account
from banking_system.branch import Branch


class Client:
    """A bank customer who holds accounts (aggregation) and may choose a
    preferred branch (association).

    Accounts are kept in a dictionary keyed by account number, because
    every account number is unique and the client looks accounts up by
    number rather than by position.
    """

    PHONE_NUMBER_LENGTH = 9
    MAXIMUM_ID_LENGTH = 9

    def __init__(
        self, client_name: str, client_id: int, phone_number: int
    ) -> None:
        if (
            isinstance(client_id, int)
            and 0 < client_id
            and len(str(client_id)) <= self.MAXIMUM_ID_LENGTH
        ):
            self.__client_id = client_id
        else:
            print("Invalid client ID, it must be 1 to 9 digits")
            self.__client_id = 0

        self.__client_name = "Unknown"
        self.__phone_number = None
        self.__accounts = {}
        self.__preferred_branch = None

        self.client_name = client_name
        self.phone_number = phone_number

    @property
    def client_id(self) -> int:
        return self.__client_id

    @property
    def client_name(self) -> str:
        return self.__client_name

    @client_name.setter
    def client_name(self, new_name: str) -> None:
        if isinstance(new_name, str) and new_name.strip() != "":
            self.__client_name = new_name
        else:
            print("Invalid name, it must be a non-empty string")

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
    def accounts(self) -> dict:
        # A copy is returned so outside code cannot add or remove
        # accounts without going through add_account().
        return dict(self.__accounts)

    @property
    def preferred_branch(self) -> Branch:
        return self.__preferred_branch

    @preferred_branch.setter
    def preferred_branch(self, branch: Branch) -> None:
        if isinstance(branch, Branch):
            self.__preferred_branch = branch
        else:
            print("Only Branch objects can be set as the preferred branch")

    def add_account(self, account: Account) -> bool:
        # Any subclass of Account is accepted, so the client does not
        # need separate logic for savings or everyday accounts.
        if not isinstance(account, Account):
            print("Only Account objects can be added")
            return False
        if account.acc_number in self.__accounts:
            print(f"Account {account.acc_number} is already held by "
                  f"this client")
            return False
        self.__accounts[account.acc_number] = account
        return True

    def has_account(self, acc_number: int) -> bool:
        return acc_number in self.__accounts

    def get_account(self, acc_number: int) -> Account:
        return self.__accounts.get(acc_number)

    def remove_account(self, acc_number: int) -> bool:
        # The account is only unlinked, it still exists afterwards.
        if self.__accounts.pop(acc_number, None) is None:
            print(f"Account {acc_number} is not held by this client")
            return False
        return True

    def total_balance(self) -> float:
        return sum(account.balance for account in self.__accounts.values())

    def month_end(self) -> dict:
        # Each account runs its own month_end(), so the client never
        # checks which kind of account it is holding.
        return {
            acc_number: account.month_end()
            for acc_number, account in self.__accounts.items()
        }

    def __eq__(self, other) -> bool:
        if not isinstance(other, Client):
            return False
        return self.__client_id == other.client_id

    def __str__(self) -> str:
        return (
            f"Client {self.__client_id}: {self.__client_name} "
            f"(phone 0{self.__phone_number}, "
            f"{len(self.__accounts)} account(s))"
        )

    def __repr__(self) -> str:
        return (
            f"Client('{self.__client_name}', {self.__client_id}, "
            f"{self.__phone_number})"
        )
