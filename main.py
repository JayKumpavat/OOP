from Transactions import Transaction
from Client import Client, Account



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