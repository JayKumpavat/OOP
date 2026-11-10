"""Shared fixtures for the Finance test suite.

Each fixture only prepares a known starting state. The behaviour being
tested always happens inside the test itself.
"""
import pytest

from banking_system.branch import Branch
from banking_system.client import Client
from banking_system.everyday_account import EverydayAccount
from banking_system.savings_account import SavingsAccount
from banking_system.transaction import Transaction
from banking_system.transfer import Transfer


@pytest.fixture
def savings():
    return SavingsAccount(1001, 500, 0.025)


@pytest.fixture
def everyday():
    return EverydayAccount(1002, 1500, "4111222233334444")


@pytest.fixture
def client():
    return Client("Alice Smith", 123456789, 412345678)


@pytest.fixture
def client_with_accounts(client, savings, everyday):
    # A client already holding one of each account type.
    client.add_account(savings)
    client.add_account(everyday)
    return client


@pytest.fixture
def everyday_with_history(everyday):
    # Deposits and withdrawals of different sizes, in a known order.
    everyday.deposit(100)
    everyday.withdraw(800, "Rent")
    everyday.withdraw(45.50, "Groceries")
    everyday.withdraw(120, "Electricity")
    return everyday


@pytest.fixture
def branch():
    return Branch(1, "Adelaide CBD", "Adelaide", 812345678)


@pytest.fixture
def savings_at_minimum():
    # A savings account sitting exactly on its minimum balance.
    return SavingsAccount(1004, 100, 0.03)


@pytest.fixture
def busy_branch(branch):
    branch.open_branch()
    branch.add_feedback("Friendly staff")
    branch.add_feedback("Long queue at lunch")
    return branch


@pytest.fixture
def deposit_record():
    return Transaction(1, "Deposit", 250, 750, "Pay")


@pytest.fixture
def withdrawal_record():
    return Transaction(2, "Withdrawal", 45.5, 704.5, "Groceries")


@pytest.fixture
def pending_transfer(everyday, savings):
    return Transfer(everyday, savings, 300)