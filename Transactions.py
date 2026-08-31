class Transaction:
    def __init__(self, transaction_id, transaction_type, t_amount, description, status='pending') -> None:
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.t_amount = t_amount
        self.description = description
        self.status = status

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
        