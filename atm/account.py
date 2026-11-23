class Account:

    def __init__(self,account_number,pin,available_balance,total_balance):
        self.account_number = account_number
        self.pin = pin
        self.available_balance = available_balance
        self.total_balance = total_balance

    def validate_pin(self,user_pin):
        if self.pin != user_pin:
            return False
        return True
        
    def get_available_balance(self):
        return self.available_balance
    
    def get_total_balance(self):
        return self.total_balance

    def credit(self,amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than Zero")
        self.total_balance += amount
        self.available_balance += amount

        
    def debit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than Zero")
        
        if self.available_balance < amount:
            raise ValueError("Insuccifient funds")

        self.available_balance -= amount
        self.total_balance -= amount







    