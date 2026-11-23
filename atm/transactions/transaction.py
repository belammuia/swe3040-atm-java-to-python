from abc import ABC, abstractmethod

class Transaction(ABC):
    def __init__(self, account_number, screen, bank_database):
        self.account_number = account_number
        self.screen = screen
        self.bank_database = bank_database
        
    @abstractmethod
    def execute(self):
        pass
