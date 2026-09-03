from BankingSystem.Accounts import Account
from BankingSystem.Client import Client
from BankingSystem.Branch import Branch
from BankingSystem.Transactions import Transaction


"""
Task 7: Demonstrate the Updated Project
Shows the Topic 3 changes: encapsulation, validation, aggregation, and association.
"""
def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------------
# 1. ENCAPSULATION
#    - Read values using getters
#    - Modify values using setters
#    - Show that behaviour-based state changes still work
# ---------------------------------------------------------------
section("1. ENCAPSULATION")

acc1 = Account(1001, "Savings", 500)

print("-- Reading values with getters --")
print("Account number:", acc1.get_acc_number())
print("Account type:", acc1.get_acc_type())
print("Balance:", acc1.get_balance())

print("\n-- Modifying values with setters --")
print(acc1.set_balance(750))          # valid change
print(acc1.set_acc_type("Business"))  # valid change
print("Balance is now:", acc1.get_balance())
print("Account type is now:", acc1.get_acc_type())

print("\n-- Behaviour-based state change (Branch open/close) --")
branch1 = Branch(1, "Adelaide Central", "Adelaide", 812345678)
branch1.open_branch()      # Closed -> Opened
branch1.open_branch()      # already Opened, cannot open again
branch1.closed_branch()    # Opened -> Closed
branch1.closed_branch()    # already Closed, cannot close again


# ---------------------------------------------------------------
# 2. VALIDATION
#    - Several valid changes
#    - Several invalid changes
#    - Confirm rejected values do not corrupt the object
# ---------------------------------------------------------------
section("2. VALIDATION")

print("Balance before invalid attempts:", acc1.get_balance())

print("\n-- Valid changes --")
print(acc1.set_balance(1200))
print(acc1.set_acc_type("Savings"))

print("\n-- Invalid changes --")
print(acc1.set_balance(-500))        # negative balance rejected
print(acc1.set_balance("lots"))      # wrong type rejected
print(acc1.set_acc_type(""))         # empty string rejected
print(acc1.set_acc_type(12345))      # wrong type rejected

print("\n-- Confirming object was not corrupted by rejected values --")
print("Balance is still:", acc1.get_balance())
print("Account type is still:", acc1.get_acc_type())


# ---------------------------------------------------------------
# 3. AGGREGATION (Client "has-a" Account, but Accounts exist
#    independently of the Client)
#    - Add different accounts to different clients
#    - Attempt to add a duplicate
#    - Attempt to add an invalid object
#    - Remove an account and confirm it still exists independently
# ---------------------------------------------------------------
section("3. AGGREGATION")

client_a = Client("Alice Smith", 100000001, 412345678)
client_b = Client("Bob Jones", 100000002, 498765432)

acc2 = Account(2002, "Checking", 250)
acc3 = Account(3003, "Savings", 900)

print("\n-- Adding different accounts to different clients --")
client_a.add_account(acc1)
client_b.add_account(acc2)
client_b.add_account(acc3)

print("\n-- Attempting to add a duplicate account --")
client_b.add_account(acc3)  # already added to client_b

print("\n-- Attempting to add an invalid object --")
client_a.add_account("not an account")  # not an Account instance

print("\n-- Client B accounts before removal --")
for acc in client_b.get_accounts():
    print(" -", acc.get_acc_number(), acc.get_acc_type())

print("\n-- Removing an account from Client B --")
client_b.remove_account(acc2)

print("\n-- Client B accounts after removal --")
for acc in client_b.get_accounts():
    print(" -", acc.get_acc_number(), acc.get_acc_type())

print("\n-- Confirming removed account still exists independently --")
print("acc2 still exists as its own object:")
acc2.display_acc_info()


# ---------------------------------------------------------------
# 4. ASSOCIATION (Client "uses-a" Branch, independent lifetimes)
#    - Select preferred branches for clients
#    - Attempt to select an invalid object
#    - Change an existing branch association
# ---------------------------------------------------------------
section("4. ASSOCIATION")

branch2 = Branch(2, "North Adelaide", "North Adelaide", 887654321)

print("-- Setting preferred branches for clients --")
client_a.set_preferred_branch(branch1)
client_b.set_preferred_branch(branch2)

print("\nAlice's preferred branch:", client_a.get_preffered_branch())
print("Bob's preferred branch:", client_b.get_preffered_branch())

print("\n-- Attempting to set an invalid object as preferred branch --")
client_a.set_preferred_branch("Not a branch object")

print("\n-- Changing an existing branch association --")
client_a.set_preferred_branch(branch2)
print(
    "Alice's preferred branch changed:",
    client_a.get_preffered_branch() is branch2,
)
