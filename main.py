from BankingSystem.Accounts import Account
from BankingSystem.Branch import Branch
from BankingSystem.Client import Client


def print_heading(title: str) -> None:
    print(f"\n=== {title} ===")


def print_transactions(account: Account) -> None:
    print(f"Transactions for account {account.acc_number}:")
    for record in account.transactions:
        print(f"  {record}")


# Setup.
acc1 = Account(1001, "Savings", 500)
acc2 = Account(1002, "Everyday", 1000)
client = Client("Alice Smith", 123456789, 412345678)
branch = Branch(1, "Adelaide CBD", "Adelaide", 812345678)

print_heading("Property syntax replaces getters")
print(acc1.acc_number, acc1.acc_type, acc1.balance)
print(client.client_id, client.client_name, client.phone_number)

print_heading("Validated property setters")
acc1.acc_type = "Fixed Deposit"
acc1.acc_type = ""
print(acc1.acc_type)
client.phone_number = 498765432
client.phone_number = 12
print(client.phone_number)

print_heading("Deposits and withdrawals create transaction records")
acc1.deposit(250)
acc1.withdraw(100)
acc2.withdraw(300, "Rent")
print_transactions(acc1)
print_transactions(acc2)

print_heading("Invalid operations create no records")
print("Negative deposit:", acc1.deposit(-50))
print("Text deposit:", acc1.deposit("100"))
print("Overdraw:", acc1.withdraw(5000))
print(f"Records on acc1: {len(acc1.transactions)}")

print_heading("Transaction history is read-only")
history = acc1.transactions
history.clear()
print(f"Cleared a copy, account still has {len(acc1.transactions)} records")

print_heading("Aggregation and association still work")
client.add_account(acc1)
client.add_account(acc2)
client.add_account(acc1)
client.preferred_branch = branch
print(client)
print(client.preferred_branch)
print(f"Total balance: ${client.total_balance():.2f}")
