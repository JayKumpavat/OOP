# from banking_system.account import Account
# from banking_system.branch import Branch
# from banking_system.client import Client
# from banking_system.everyday_account import EverydayAccount
# from banking_system.savings_account import SavingsAccount


# def print_heading(title: str) -> None:
#     print(f"\n=== {title} ===")


# def print_transactions(account: Account) -> None:
#     print(f"Transactions for account {account.acc_number}:")
#     for record in account.transactions:
#         print(f"  {record}")


# # Setup.
# savings = SavingsAccount(1001, 500, 0.025)
# everyday = EverydayAccount(1002, 2000, "4111222233334444")
# client = Client("Alice Smith", 123456789, 412345678)
# adelaide_branch = Branch(1, "Adelaide CBD", "Adelaide", 812345678)
# glenelg_branch = Branch(2, "Glenelg", "Glenelg", 812345679)

# print_heading("Properties (read-only and validated)")
# print(savings.acc_number, savings.balance, savings.interest_rate)
# print(everyday.masked_card_number)
# client.phone_number = 498765432
# print(client.phone_number)
# client.phone_number = 12
# print(client.phone_number)

# print_heading("Client aggregation with different account types")
# client.add_account(savings)
# client.add_account(everyday)
# client.add_account(savings)
# for account in client.accounts:
#     print(account)
# print(f"Total balance: ${client.total_balance():.2f}")

# print_heading("Inherited deposit behaviour")
# savings.deposit(250)
# everyday.deposit(100)
# print(savings)
# print(everyday)

# print_heading("Overridden withdraw behaviour")
# print("Valid savings withdrawal:", savings.withdraw(300))
# print("Savings below minimum:", savings.withdraw(400))
# print("Valid everyday withdrawal:", everyday.withdraw(800))
# print("Everyday above limit:", everyday.withdraw(1500))

# print_heading("Invalid operations create no records")
# print("Negative deposit:", everyday.deposit(-50))
# print("Text withdrawal:", everyday.withdraw("100"))
# savings.apply_interest()
# print_transactions(savings)
# print_transactions(everyday)

# print_heading("isinstance() with the hierarchy")
# print("Savings is an Account:", isinstance(savings, Account))
# print("Everyday is an Account:", isinstance(everyday, Account))
# print("Savings is a SavingsAccount:", isinstance(savings, SavingsAccount))
# print("Savings is an EverydayAccount:", isinstance(savings, EverydayAccount))
# print("Concrete types:", type(savings).__name__, type(everyday).__name__)

# print_heading("Association with a branch")
# client.preferred_branch = adelaide_branch
# client.preferred_branch = "not a branch"
# print(client.preferred_branch)
# client.preferred_branch = glenelg_branch
# glenelg_branch.open_branch()
# glenelg_branch.open_branch()
# glenelg_branch.add_feedback("Friendly staff and short queues.")
# print(client.preferred_branch)
# print(glenelg_branch.feedback)

# print_heading("Removing an account keeps it alive")
# client.remove_account(everyday)
# print(client)
# print(everyday)