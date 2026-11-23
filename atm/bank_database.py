class BankDatabase:

    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def get_account(self, account_number):
        retrieved_account = self.accounts.get(account_number)
        return retrieved_account

    def authenticate_user(self, account_number,pin):
        account = self.get_account(account_number)
        if not account:
            return False
        return account.validate_pin(pin)

    def get_available_balance(self,account_number):
        account = self.get_account(account_number)
        if not account:
            raise ValueError("Account not found")
        return account.get_available_balance()
    
    def get_total_balance(self, account_number):
        account = self.get_account(account_number)
        if not account:
            raise ValueError("Account not found")
        return account.get_total_balance()     

    def credit(self, account_number, amount):
        account = self.get_account(account_number)
        if not account:
            raise ValueError("Account not found")

        return account.credit(amount)

    def debit(self, account_number, amount):
        account = self.get_account(account_number)
        if not account:
            raise ValueError("Account not found")

        return account.debit(amount)