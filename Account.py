class Account:
    def __init__(self, acc_number, acc_type, balance):
        self.acc_number = acc_number
        self.acc_type = acc_type
        self.balance = balance

    def display_acc_info(self):
        print(f"Account No: {self.acc_number}")
        print(f"Account Type: {self.acc_type}")
        print(f"Account Balance: ${self.balance}")