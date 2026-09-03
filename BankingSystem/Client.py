from Accounts import Account
from Branch import Branch


class Client:
    def __init__(
        self,
        client_name: str,
        client_id: int,
        client_no: int,
    ):
        if isinstance(client_name, str):
            self.__client_name = client_name
        else:
            print("Enter a valid name, it must only contain letters")

        if isinstance(client_id, int):
            self.__client_id = client_id
        else:
            print("Enter a client id that is only numbers and no spaces in between or symbols")

        if isinstance(client_no, int) and len(str(client_id)) == 9:
            self.__client_no = client_no
        else:
            print("Enter a valid phone with 9 digits not including 0")

        self.__accounts = []
        self.__preferred_branch = None

    # Displays client information (name, client_id, client_phone_number)
    def display_client_info(self):
        print("Client ID:", self.__client_id)
        print("Client Name:", self.__client_name)
        print("Client Number:", self.__client_no)

    # Adds an existing Account ot this client (aggregation)
    def add_account(self, account):
        if not isinstance(account, Account):
            print("Only Account objects can be added")
            return

        if account in self.__accounts:
            print("This account has already been added to this client")
            return

        self.__accounts.append(account)
        print("Account added to client")

    # Removes an Account from this client without destroying the account
    def remove_account(self, account):
        if account not in self.__accounts:
            print("This account is not assigned to this client")
            return

        self.__accounts.remove(account)
        print("Account removed from client")

    def get_accounts(self):
        return list(self.__accounts)

    # This function allows client to update their phone number
    def set_change_client_number(self, new_number):
        if isinstance(new_number, int) and len(str(new_number)) == 9:
            self.__client_no = new_number
            print("Client number updated to:", self.__client_no)
        else:
            print(f"phone number must have 9 numbers (not including 0)")

    # Allows bank to change their name
    def set_client_name(self, new_name):
        if isinstance(new_name, str):
            self.__client_name = new_name
            return f"Name has been changed to {self.__client_name}"
        else:
            print(f"The client name cannot have numbers or symbols, please try again")

    # Allows bank to change client_id
    def set_client_id(self, new_id):
        if isinstance(new_id, int) and len(str(new_id)) <= 9:
            self.__client_id = new_id
            return f"client Id has been changed to: {self.__client_id}"
        else:
            print(f"the new client_id must be between 1 - 9 digits")

    # str for showing client information in readable form
    def __str__(self):
        print(
            f"Client's Id is {self.__client_id} and client name is {self.__client_name} and their phone number is {self.__client_no}"
        )

    # repr to just show important information
    def __repr__(self):
        print(f"Client Id: {self.__client_id}\n\
            Client Name: {self.__client_name}\n\
            Client Phone Number: {self.__client_no}")
