from atm.transactions.transaction import Transaction


class BalanceInquiry(Transaction):

    def __init__(self, account_number, screen, bank_database):
        super().__init__(account_number, screen, bank_database)

    def execute(self):
        available_balance = self.bank_database.get_available_balance(
            self.account_number
        )
        total_balance = self.bank_database.get_total_balance(
            self.account_number
        )

        self.screen.display_message("Available balance:")
        self.screen.display_dollar_amount(available_balance)

        self.screen.display_message("Total balance:")
        self.screen.display_dollar_amount(total_balance)