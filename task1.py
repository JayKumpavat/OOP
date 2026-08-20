from Transaction import Transaction

class Client:
    def __init__(
        self,
        client_name,
        client_id,
        client_no,
    ):
        self.client_name = client_name
        self.client_id = client_id
        self.client_no = client_no

    def display_client_info(self):
        print("Client ID:", self.client_id)
        print("Client Name:", self.client_name)
        print("Client Number:", self.client_no)

    def change_client_number(self, new_number):
        self.client_no = new_number
        print("Client number updated to:", self.client_no)


class Account:
    def __init__(self, acc_number, acc_type, balance):
        self.acc_number = acc_number
        self.acc_type = acc_type
        self.balance = balance

    def display_acc_info(self):
        print(f"Account No: {self.acc_number}")
        print(f"Account Type: {self.acc_type}")
        print(f"Account Balance: ${self.balance}")

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(
            f"${deposit_amount} has been added to {self.acc_type}, new balance: ${self.balance}"
        )

    def withdrawl(self, withdrawl_amount):
        if self.balance <= withdrawl_amount:
            print(f"insufficient Balance, Withdrawl Denied")
        else:
            self.balance -= withdrawl_amount
            print(
                f"{withdrawl_amount} has been withdrawn from your account, new balance: ${self.balance}"
            )

    def viewbalance(self):
        print(f"Your {self.acc_type} account balacne is: ${self.balance}")


#class Transaction:
#    def __init__(self, acount_a, acount_b, transfer_amount):
#        self.acount_a = acount_a
#        self.acount_b = acount_b
#        self.transfer_amount = transfer_amount

#    def transfering_ammount(self, acount_a, acount_b, transfer_amount):
#        if acount_a.balance <= transfer_amount:
#            print(f"insufficient Balance, Withdrawl Denied")
#        else:
#            acount_a.balance -= transfer_amount
#            acount_b.balance += transfer_amount
#            print(f"{acount_a.acc_number} now has ${acount_a.balance}")
#            print(f"{acount_b.acc_number} now has {acount_b.balance}")


Client1 = Client("John Doe", "00001", "555-1234")
Client2 = Client("Toby Maguire", "00002", "555-1235")
Account1 = Account(1101, "Savings", 10000)
Account2 = Account(1102, "Savings", 500)



transfering = Transaction(1, Account1, Account2, 500, 'Moving money to savings',)
transfering.transfering(1, Account1, Account2, 500, 'Moving money to savings', 'pending')