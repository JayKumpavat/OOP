from banking_system.account import Account
from banking_system.branch import Branch
from banking_system.client import Client
from banking_system.everyday_account import EverydayAccount
from banking_system.savings_account import SavingsAccount
from banking_system.transfer import Transfer


def print_heading(title: str) -> None:
    print(f"\n=== {title} ===")


# Setup.
client = Client("Alice Smith", 123456789, 412345678)
adelaide_branch = Branch(1, "Adelaide CBD", "Adelaide", 812345678)
glenelg_branch = Branch(2, "Glenelg", "Glenelg", 812345679)

print_heading("Account is abstract")
print("Abstract methods on Account:", sorted(Account.__abstractmethods__))

print_heading("Dictionary: client accounts keyed by account number")
client.add_account(SavingsAccount(1001, 500, 0.025))
client.add_account(EverydayAccount(1002, 2000, "4111222233334444"))
client.add_account(SavingsAccount(1003, 3000, 0.04))
client.add_account(SavingsAccount(1001, 999, 0.01))
client.add_account("not an account")
for acc_number, account in client.accounts.items():
    print(f"{acc_number}: {account}")
print("Holds 1002?", client.has_account(1002))
print("Holds 9999?", client.has_account(9999))
print(f"Total balance: ${client.total_balance():.2f}")
print(f"{client.client_name} has {len(client.accounts)} accounts")

print_heading("Retrieve accounts by number and use them")
savings = client.get_account(1001)
everyday = client.get_account(1002)
print("Account 9999:", client.get_account(9999))
savings.deposit(250)
savings.withdraw(300)
everyday.deposit(100)
everyday.withdraw(800, "Rent")
everyday.withdraw(45.50, "Groceries")
everyday.withdraw(120, "Electricity")

print_heading("Specialised withdraw rules still apply")
print("Savings below minimum:", savings.withdraw(400))
print("Everyday above limit:", everyday.withdraw(1500))
print("Negative deposit:", everyday.deposit(-50))

print_heading("List: transaction history in the order it was recorded")
print(everyday.statement())
print(f"Number of transactions: {everyday.transaction_count()}")
print("Withdrawals only:")
for record in everyday.transactions_of_type("Withdrawal"):
    print(f"  {record}")
print("Transactions above $100:")
for record in everyday.transactions_above(100):
    print(f"  {record}")

print("Latest everyday record:", everyday.transactions[-1])

print_heading("Polymorphic month end across every account")
print(f"Savings interest rate: {savings.interest_rate * 100:.1f}%")
for acc_number, posted in client.month_end().items():
    print(f"{acc_number}: posted {posted}")
for account in client.accounts.values():
    print(account)

print_heading("Transfer between accounts")
transfer = Transfer(everyday, savings, 200)
transfer.execute()
print(transfer)
transfer.execute()
print(savings.statement())

print_heading("isinstance() with the hierarchy")
print("Savings is an Account:", isinstance(savings, Account))
print("Everyday is an Account:", isinstance(everyday, Account))
print("Savings is an EverydayAccount:", isinstance(savings, EverydayAccount))

print_heading("Association with a branch")
client.preferred_branch = adelaide_branch
client.preferred_branch = "not a branch"
client.preferred_branch = glenelg_branch
glenelg_branch.open_branch()
glenelg_branch.add_feedback("Friendly staff and short queues.")
print(client.preferred_branch)
print(glenelg_branch.feedback)

print_heading("Removing an account by number keeps it alive")
client.remove_account(1003)
client.remove_account(1003)
print(client)
print(everyday)