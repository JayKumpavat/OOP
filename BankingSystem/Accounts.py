class Account:
    def __init__(self, acc_number, acc_type, balance):
        self.__acc_number = acc_number
        self.__acc_type = acc_type
        self.__balance = balance

    # display's Account information
    def display_acc_info(self):
        print(f"Account No: {self.__acc_number}")
        print(f"Account Type: {self.__acc_type}")
        print(f"Account Balance: ${self.__balance}")

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
