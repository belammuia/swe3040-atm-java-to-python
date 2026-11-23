class CashDispenser:
    def __init__(self, atm_balance):
        self.atm_balance = atm_balance

    def is_sufficient_cash_available(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        if amount > self.atm_balance:
            return False
        return True
    
    def dispense_cash(self, amount):
        sufficient = self.is_sufficient_cash_available(amount)

        if sufficient:
            self.atm_balance -= amount
            return True
        return False
        
