from atm.transactions.transaction import Transaction

class Deposit(Transaction):
    def __init__(self, account_number, screen, bank_database,
                 keypad, deposit_slot):
        super().__init__(account_number, screen, bank_database)
        self.keypad = keypad
        self.deposit_slot = deposit_slot

    def execute(self):
        self.screen.display_message("Enter deposit amount:")
        amount = float(self.keypad.get_input("Amount: "))

        if amount <= 0:
            self.screen.display_message("Invalid deposit amount.")
            return

        self.screen.display_message("Insert your deposit envelope.")

        if not self.deposit_slot.is_envelope_received():
            self.screen.display_message("No envelope received. Deposit cancelled.")
            return

        self.bank_database.credit(self.account_number, amount)

        self.screen.display_message("Successfully deposited.")
        self.screen.display_dollar_amount(amount)