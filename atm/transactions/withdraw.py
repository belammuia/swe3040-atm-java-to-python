from atm.transactions.transaction import Transaction


class Withdrawal(Transaction):

    def __init__(self, account_number, screen, bank_database,
                 keypad, cash_dispenser):
        super().__init__(account_number, screen, bank_database)
        self.keypad = keypad
        self.cash_dispenser = cash_dispenser

    def execute(self):
        self.screen.display_message("Enter withdrawal amount:")
        amount = float(self.keypad.get_input("Amount: "))

        if amount <= 0:
            self.screen.display_message("Invalid withdrawal amount.")
            return

        available_balance = self.bank_database.get_available_balance(
            self.account_number
        )

        if amount > available_balance:
            self.screen.display_message("Insufficient account funds.")
            return

        if not self.cash_dispenser.is_sufficient_cash_available(amount):
            self.screen.display_message("Insufficient ATM cash.")
            return

        self.bank_database.debit(self.account_number, amount)
        self.cash_dispenser.dispense_cash(amount)

        self.screen.display_message("Please take your cash.")
        self.screen.display_dollar_amount(amount)