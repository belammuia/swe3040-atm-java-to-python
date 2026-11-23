from atm.bank_database import BankDatabase
from atm.screen import Screen
from atm.keypad import Keypad
from atm.transactions.cash_dispenser import CashDispenser
from atm.deposit_slot import DepositSlot

from atm.transactions.balance_inquiry import BalanceInquiry
from atm.transactions.withdraw import Withdrawal
from atm.transactions.deposit import Deposit


class ATM:
    def __init__(self):
        self.screen = Screen()
        self.keypad = Keypad()
        self.cash_dispenser = CashDispenser(100000)
        self.deposit_slot = DepositSlot()
        self.bank_database = BankDatabase()

        self.current_account_number = None

    def authenticate_user(self):
        account_number = self.keypad.get_input("Enter account number: ")
        pin = self.keypad.get_input("Enter PIN: ")

        if self.bank_database.authenticate_user(account_number, pin):
            self.current_account_number = account_number
            return True

        self.screen.display_message("Invalid account number or PIN.")
        return False

    def display_menu(self):
        self.screen.display_message(
            "\n1. Balance Inquiry\n"
            "2. Withdrawal\n"
            "3. Deposit\n"
            "4. Exit"
        )
        return self.keypad.get_input("Select an option: ")

    def perform_transactions(self):
        while True:
            choice = self.display_menu()

            if choice == "1":
                transaction = BalanceInquiry(
                    self.current_account_number,
                    self.screen,
                    self.bank_database
                )

            elif choice == "2":
                transaction = Withdrawal(
                    self.current_account_number,
                    self.screen,
                    self.bank_database,
                    self.keypad,
                    self.cash_dispenser
                )

            elif choice == "3":
                transaction = Deposit(
                    self.current_account_number,
                    self.screen,
                    self.bank_database,
                    self.keypad,
                    self.deposit_slot
                )

            elif choice == "4":
                self.screen.display_message("Thank you for using our ATM.")
                break

            else:
                self.screen.display_message("Invalid selection.")
                continue

            transaction.execute()

    def run(self):
        if self.authenticate_user():
            self.perform_transactions()