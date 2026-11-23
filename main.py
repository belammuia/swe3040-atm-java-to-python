from atm.atm import ATM
from atm.account import Account


def main():
    atm = ATM()

    account1 = Account(
        account_number="123456",
        pin="1234",
        available_balance=50000,
        total_balance=50000
    )

    account2 = Account(
        account_number="654321",
        pin="5678",
        available_balance=100000,
        total_balance=100000
    )

    atm.bank_database.add_account(account1)
    atm.bank_database.add_account(account2)

    atm.run()


if __name__ == "__main__":
    main()