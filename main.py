from BankingSystem.Accounts import Account
from BankingSystem.Client import Client
from BankingSystem.Branch import Branch
from BankingSystem.Transactions import Transaction


print("========== 1. ENCAPSULATION ==========\n")

client_a = Client("Alex Smith", 123456789, 412345678)

# Reading values: Client has no direct name/id/phone getters, so
# display_client_info() is the read-access method available.
print("-- Initial client info (read via display_client_info) --")
client_a.display_client_info()

# Modifying values using setters
print("\n-- Changing name and phone number using setters --")
client_a.set_client_name("Alexandra Smith")
client_a.set_change_client_number(498765432)

print("\n-- Client info after setter changes --")
client_a.display_client_info()

# Behaviour-based state change (not a plain setter): Transaction.process()
print("\n-- Behaviour-based state change: Transaction.process() --")
txn = Transaction(1, "Deposit", 200, "Initial deposit")
print(txn.process())          # Pending -> Completed
print(txn.process())          # already Completed, should be rejected


print("\n========== 2. VALIDATION ==========\n")

print("-- Valid changes --")
client_a.set_client_name("Alexandra J Smith")           # valid str
client_a.set_change_client_number(411112222)            # valid 9-digit int

print("\n-- Invalid changes --")
client_a.set_client_name(12345)                         # not a string, rejected
client_a.set_change_client_number(123)                  # wrong digit length, rejected

print("\n-- Confirming object was not corrupted by invalid input --")
client_a.display_client_info()

print("\n-- Branch validation --")
branch_1 = Branch(1, "Adelaide City Branch", "Adelaide", 812345678)
print(branch_1.set_change_branch_name("Adelaide Central Branch"))  # valid
branch_1.set_change_branch_name(999)                                # invalid, rejected
branch_1.set_upd_branch_no(812223344)                               # valid, 9 digits
branch_1.set_upd_branch_no(5)                                       # invalid, rejected


print("\n========== 3. AGGREGATION (Client - Account) ==========\n")

client_b = Client("Sam Chen", 222222222, 422222222)

acc_1 = Account(1001, "Savings", 500)
acc_2 = Account(1002, "Checking", 1000)
acc_3 = Account(1003, "Savings", 250)

# Add different accounts to different clients
client_a.add_account(acc_1)
client_b.add_account(acc_2)
client_b.add_account(acc_3)

print("client_a account count:", len(client_a.get_accounts()))
print("client_b account count:", len(client_b.get_accounts()))

# Attempt to add a duplicate
print("\n-- Attempting duplicate add --")
client_a.add_account(acc_1)

# Attempt to add an invalid object
print("\n-- Attempting to add an invalid object --")
client_a.add_account("not an account")

# Remove an account and confirm it still exists independently
print("\n-- Removing acc_1 from client_a --")
client_a.remove_account(acc_1)
print("client_a account count after removal:", len(client_a.get_accounts()))
print("acc_1 still exists on its own:")
acc_1.display_acc_info()


print("\n========== 4. ASSOCIATION (Client - Branch) ==========\n")

branch_2 = Branch(2, "Norwood Branch", "Norwood", 812345679)

# Select preferred branches for different clients
client_a.set_preferred_branch(branch_1)
client_b.set_preferred_branch(branch_2)

print("client_a preferred branch is branch_1:", client_a.get_preffered_branch() is branch_1)
print("client_b preferred branch is branch_2:", client_b.get_preffered_branch() is branch_2)

# Attempt to select an invalid object
print("\n-- Attempting to set an invalid preferred branch --")
client_a.set_preferred_branch("not a branch")

# Change an existing branch association
print("\n-- Changing client_a's preferred branch --")
client_a.set_preferred_branch(branch_2)
print("client_a preferred branch is now branch_2:", client_a.get_preffered_branch() is branch_2)
print("client_b preferred branch is unaffected:", client_b.get_preffered_branch() is branch_2)
