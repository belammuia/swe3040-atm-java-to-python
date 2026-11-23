# ATM Case Study: Java to Python Migration

## Overview

This project implements an Automated Teller Machine (ATM) system in Python, migrated from the original Java implementation in Chapter 34: *ATM Case Study Part 2 – Implementing the Design*.

The application demonstrates object-oriented programming concepts through a simulated ATM that supports authentication, balance inquiries, withdrawals and deposits.

## Features

- User authentication using account numbers and PINs.
- Available and total balance inquiries.
- Cash withdrawals with account balance and ATM cash availability checks.
- Deposits with envelope receipt simulation.
- Transaction handling using inheritance and polymorphism.
- Modular code organisation using Python packages.

## Project Structure

```text
swe3040-atm-java-to-python/
├── atm/
│   ├── __init__.py
│   ├── atm.py
│   ├── account.py
│   ├── bank_database.py
│   ├── screen.py
│   ├── keypad.py
│   ├── deposit_slot.py
│   └── transactions/
│       ├── __init__.py
│       ├── transaction.py
│       ├── balance_inquiry.py
│       ├── withdraw.py
│       ├── deposit.py
│       └── cash_dispenser.py
├── main.py
└── README.md
```

## Requirements

- Python 3.10 or later

No external dependencies are required.

## Running the Application

Clone the repository:

```bash
git clone git@github.com:belammuia/swe3040-atm-java-to-python.git
cd swe3040-atm-java-to-python
```

Run the application:

```bash
python main.py
```

## Sample Accounts

| Account Number | PIN | Initial Balance |
|---|---|---:|
| 123456 | 1234 | 50,000 |
| 654321 | 5678 | 100,000 |

## Object-Oriented Concepts Demonstrated

- **Encapsulation:** Account data and operations are managed within the Account class.
- **Inheritance:** BalanceInquiry, Withdrawal and Deposit inherit from Transaction.
- **Abstraction:** Transaction uses Python's Abstract Base Class mechanism.
- **Polymorphism:** Different transaction objects implement their own `execute()` method.
- **Composition:** The ATM coordinates multiple collaborating components.

## Technologies

- Python
- Git
- GitHub

## Academic Context

Course: SWE3040A  
Project: ATM Case Study – Java to Python Migration

Reference: Chapter 34, *ATM Case Study Part 2: Implementing the Design*.
