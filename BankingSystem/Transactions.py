class Transaction:
    def __init__(self, transaction_id: int, transaction_type: str, t_amount: int, description: str) -> None:
        self.__transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.t_amount = t_amount
        self.description = description
        self.status = "Pending"

# Depositing money 
    def deposit(self, my_account, deposit_amount):
        if isinstance(deposit_amount, (int,float)):
            self.balance += deposit_amount
            print(
                f"${deposit_amount} has been added to {my_account.acc_type}, new balance: ${my_account.balance}"
            )
        else:
            print(f"incorrect deposit amount, should be int")

#withdrawl money
    def withdrawl(self, my_account, withdrawl_amount: int):
        if isinstance(withdrawl_amount, (int,float)) and my_account.balance >= withdrawl_amount:
            my_account.balance -= withdrawl_amount
            print(
                f"{withdrawl_amount} has been withdrawn from your account, new balance: ${my_account.balance}"
            )
        else:
            print(f"insufficient Balance, Withdrawl Denied")

#viewing account balance
    def viewbalance(self, my_account):
        print(f"Your {my_account.acc_type} account balacne is: ${my_account.acc_type}")

#transfering money betwen two accounts
    def transfering(self, transaction_id: int, account_a, account_b, t_amount: int, description: str):
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
                  f'status: {self.status}\n')

# changing process from completed -> Cancelled
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
        if isinstance(new_desc, str):
            self.description = new_desc
            return f"the description has been changed to: {new_desc}"

# __str__ and __repr__
    def __str__(self):
        print(f"The transaction that is conducted is a {self.transaction_type}, with amount {self.t_amount}, and the status is {self.status}")

    def __repr__(self):
        print(f"transaction id: {self.__transaction_id} \n\
transaction type: {self.transaction_type} \n\
transaction amount: {self.t_amount} \n\
transaction description: {self.description}\n\
status: {self.status}")




        