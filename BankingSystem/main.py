from Accounts import Account
from Client import Client
from Branch import Branch
from Transactions import Transaction

# Setup 
acc1 = Account(1001, "Savings", 500)
acc2 = Account(1002, "Checking", 1000)
acc3 = Account(1003, "Savings", 250)

client1 = Client("Alice Smith", 123456789, 412345678)
client2 = Client("Bob Jones", 987654321, 498765432)

branch1 = Branch(1, "Adelaide CBD", "Adelaide", 812345678)
branch2 = Branch(2, "Glenelg", "Glenelg", 812345679)

transaction1 = Transaction(1, "Deposit", 500, "Initial deposit")


# 1. Encapsulation
print("testing getter values")
print(acc1.get_acc_number())
print(acc1.get_acc_type())
print(acc1.get_balance())

print("testing setter - valid account type change")
print(acc1.set_acc_type("Fixed Deposit"))
print(acc1.get_acc_type())

print("testing setter - valid balance change")
print(acc1.set_balance(750))
print(acc1.get_balance())

print("testing behaviour-based state change - transaction process")
print(transaction1.process())

print("testing behaviour-based state change - branch open")
branch1.open_branch()


# 2. Validation 
print("testing invalid setter - empty string account type")
print(acc1.set_acc_type(""))
print(acc1.get_acc_type())

print("testing invalid setter - non-string account type")
print(acc1.set_acc_type(123))
print(acc1.get_acc_type())

print("testing invalid setter - negative balance")
print(acc1.set_balance(-100))
print(acc1.get_balance())

print("testing invalid setter - non-numeric balance")
print(acc1.set_balance("500"))
print(acc1.get_balance())

print("testing invalid behaviour - processing an already completed transaction")
print(transaction1.process())

print("testing invalid behaviour - opening an already opened branch")
branch1.open_branch()


# 3. Aggregation 
print("testing aggregation - adding accounts to clients")
client1.add_account(acc1)
client1.add_account(acc2)
client2.add_account(acc3)
print([a.get_acc_number() for a in client1.get_accounts()])
print([a.get_acc_number() for a in client2.get_accounts()])

print("testing aggregation - adding a duplicate account")
client1.add_account(acc1)
print([a.get_acc_number() for a in client1.get_accounts()])

print("testing aggregation - adding an invalid object")
client1.add_account("not an account")
print([a.get_acc_number() for a in client1.get_accounts()])

print("testing aggregation - removing an account from client")
client1.remove_account(acc2)
print([a.get_acc_number() for a in client1.get_accounts()])
print(acc2.get_acc_number())


# 4. Association 
print("testing association - setting preferred branch")
client1.set_preferred_branch(branch1)
print(client1.get_preffered_branch().get_branch_name())

print("testing association - setting an invalid object as preferred branch")
client1.set_preferred_branch("not a branch")
print(client1.get_preffered_branch().get_branch_name())

print("testing association - changing preferred branch")
client1.set_preferred_branch(branch2)
print(client1.get_preffered_branch().get_branch_name())
