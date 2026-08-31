from Transactions import Transaction
from Client import Client
from Accounts import Account



Client1 = Client("John Doe", "00001", "555-1234")
Client2 = Client("Toby Maguire", "00002", "555-1235")
Account1 = Account(1101, "Savings", 10000)
Account2 = Account(1102, "Savings", 500)



transfering = Transaction(1, "money_transfer", 10000, "Moving Money to savings")
#transfering.transfering(1, Account1, Account2, 500, 'Moving money to savings', 'pending')
transfering.withdrawl(Account1, 1000)

