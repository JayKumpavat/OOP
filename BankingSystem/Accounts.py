class Account:
    def __init__(
            self, 
            acc_number: int, 
            acc_type: str, 
            balance
            ) -> None:

        #Isisntance is used to verify the datatype entered into the class

        if isinstance(acc_number, int):
            self.__acc_number = acc_number

        if isinstance(acc_type, str):
            self.__acc_type = acc_type

        if isinstance(balance, (int,float)):
            self.__balance = balance

    # Display's account information which includes the account number, account type (savings, credit etc) and account balance
    def display_acc_info(self):
        print(f"Account No: {self.__acc_number}")
        print(f"Account Type: {self.__acc_type}")
        print(f"Account Balance: ${self.__balance}")

    # the 3 get_... are used to read private attributes of the account class
    def get_acc_number(self):
        return self.__acc_number
 
    def get_acc_type(self):
        return self.__acc_type
 
    def get_balance(self):
        return self.__balance

    #Setters validated access to private attributes
    def set_acc_type(self, new_type: str):
        if isinstance(new_type, str) and new_type.strip() != "":
            self.__acc_type = new_type
            return f"Account type updated to: {self.__acc_type}"
        else:
            return "Invalid account type, it must be a non-empty string"
 
    def set_balance(self, new_balance):
        if isinstance(new_balance, (int, float)) and new_balance >= 0:
            self.__balance = new_balance
            return f"Balance updated to: ${self.__balance}"
        else:
            return "Invalid balance, it must be a non-negative number"

    # Str representation of account information.
    def __str__(self):
        print(
            f"The account number is {self.__acc_number}, and it is a {self.__acc_type} account with a balance of ${self.__balance}"
        )

    # Repr for account info.
    def __repr__(self):
        print(
            f"Account No: {self.__acc_number}\n"
            f"Account Type: {self.__acc_type} \n"
            f"Account Balance: {self.__balance}"
        )
