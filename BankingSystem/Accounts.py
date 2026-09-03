class Account:
    def __init__(
            self, 
            acc_number: int, 
            acc_type: str, 
            balance
            ) -> None:

        if isinstance(acc_number, int):
            self.__acc_number = acc_number

        if isinstance(acc_type, str):
            self.__acc_type = acc_type

        if isinstance(balance, (int,float)):
            self.__balance = balance

    # display's Account information
    def display_acc_info(self):
        print(f"Account No: {self.__acc_number}")
        print(f"Account Type: {self.__acc_type}")
        print(f"Account Balance: ${self.__balance}")

    def get_acc_number(self):
        return self.__acc_number
 
    def get_acc_type(self):
        return self.__acc_type
 
    def get_balance(self):
        return self.__balance

    # str representation of account information
    def __str__(self):
        print(
            f"The account number is {self.__acc_number}, and it is a {self.__acc_type} account with a balance of ${self.__balance}"
        )

    # repr for account info
    def __repr__(self):
        print(
            f"Account No: {self.__acc_number}\n"
            f"Account Type: {self.__acc_type} \n"
            f"Account Balance: {self.__balance}"
        )
