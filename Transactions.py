import Accounts

class Transaction:
    def __init__(self, transaction_id, transaction_type, t_amount, description) -> None:
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.t_amount = t_amount
        self.description = description
        self.status = "Pending"

    def deposit(self, deposit_amount, acc_type):
        self.balance += deposit_amount
        print(
            f"${deposit_amount} has been added to {acc_type}, new balance: ${self.balance}"
        )

    def withdrawl(self, my_account, withdrawl_amount):
        if my_account.balance <= withdrawl_amount:
            print(f"insufficient Balance, Withdrawl Denied")
        else:
            my_account.balance -= withdrawl_amount
            print(
                f"{withdrawl_amount} has been withdrawn from your account, new balance: ${self.balance}"
            )

    def viewbalance(self, acc_type):
        print(f"Your {acc_type} account balacne is: ${self.balance}")

    def transfering(self, transaction_id, account_a, account_b, t_amount, description, status):
        if account_a.balance < t_amount:
            return f'Insuffient Balance, Try Again'
        else:
            account_a.balance -= t_amount
            account_b.balance += t_amount

            print(f'Transaction ID: {transaction_id} \n'
                  f'Account Number (Withdrawl): {account_a.acc_number} \n'
                  f'{account_a.acc_type}: {account_a.balance} \n'
                  f'Account Number (Deposit): {account_b.acc_number} \n'
                  f'{account_b.acc_type}: {account_b.balance}\n'
                  f'Transfer Description: {description}\n'
                  f'status: {status}\n')

    def process(self):
        if self.status == "Pending":
            self.status = "Completed"
            return f"Your status is now {self.status}"
        else:
            return f"Could not complete status because it is {self.status}"

    def cancelled(self):
        if self.status == "Pending":
            self.status = "Cancelled"
            return f"The Transaction was {self.status}"
        else:
            return f"The transaction could not be cancelled as it is {self.status}"

    def change_desc(self, new_desc: str):
        self.description = new_desc
        return f"the description has been changed to: {new_desc}"




        