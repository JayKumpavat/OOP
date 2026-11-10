"""Tests for the Account hierarchy and its transaction history."""
import pytest

from banking_system.account import Account
from banking_system.everyday_account import EverydayAccount
from banking_system.savings_account import SavingsAccount


def make_accounts():
    return [
        SavingsAccount(2001, 1000, 0.02),
        EverydayAccount(2002, 1000, "1234123412341234"),
    ]


class TestAbstractAccount:
    def test_account_cannot_be_created_directly(self):
        with pytest.raises(TypeError):
            Account(1, 100)

    def test_invalid_account_number_uses_zero(self):
        assert SavingsAccount(-5, 100, 0.02).acc_number == 0
        assert EverydayAccount("1", 100, "1234123412341234").acc_number == 0

    @pytest.mark.parametrize("opening", [-10, "500", True])
    def test_invalid_opening_balance_starts_at_zero(self, opening):
        account = EverydayAccount(3001, opening, "1234123412341234")
        assert account.balance == 0


class TestSharedBehaviour:
    """Shared Account behaviour, tested through each concrete type."""

    @pytest.mark.parametrize("account", make_accounts())
    def test_deposit_increases_balance(self, account):
        assert account.deposit(250) is True
        assert account.balance == 1250

    @pytest.mark.parametrize("account", make_accounts())
    @pytest.mark.parametrize("amount", [0, -50, "100", True])
    def test_invalid_deposit_changes_nothing(self, account, amount):
        assert account.deposit(amount) is False
        assert account.balance == 1000
        assert account.transaction_count() == 0

    @pytest.mark.parametrize("account", make_accounts())
    def test_withdraw_decreases_balance(self, account):
        assert account.withdraw(300) is True
        assert account.balance == 700

    @pytest.mark.parametrize("account", make_accounts())
    def test_invalid_withdrawal_changes_nothing(self, account):
        assert account.withdraw(-1) is False
        assert account.balance == 1000
        assert account.transaction_count() == 0

    def test_cannot_withdraw_more_than_balance(self):
        account = EverydayAccount(3002, 50, "1234123412341234")
        assert account.withdraw(60) is False
        assert account.balance == 50

    def test_accounts_are_equal_by_number(self, savings):
        assert savings == SavingsAccount(1001, 0, 0.01)
        assert savings != "1001"

    def test_repr_names_the_concrete_type(self, savings):
        assert repr(savings).startswith("SavingsAccount(acc_number=1001")


class TestSavingsAccount:
    def test_valid_withdrawal(self, savings):
        assert savings.withdraw(400) is True
        assert savings.balance == 100

    def test_minimum_balance_is_enforced(self, savings):
        assert savings.withdraw(401) is False
        assert savings.balance == 500
        assert savings.transactions == []

    @pytest.mark.parametrize("rate", [-0.01, 0.11, "2%"])
    def test_invalid_interest_rate_uses_zero(self, rate):
        account = SavingsAccount(1005, 500, rate)
        assert account.interest_rate == 0

    def test_apply_interest_records_a_deposit(self, savings):
        assert savings.apply_interest() is True
        assert savings.balance == pytest.approx(512.50)
        assert savings.transactions[-1].transaction_type == "Deposit"

    def test_zero_rate_posts_no_interest(self):
        account = SavingsAccount(1006, 500, 0)
        assert account.apply_interest() is False
        assert account.transaction_count() == 0

    def test_month_end_applies_interest(self, savings):
        assert savings.month_end() is True
        assert savings.balance == pytest.approx(512.50)

    def test_str_shows_rate(self, savings):
        assert str(savings).endswith("(interest rate 2.5%)")


class TestEverydayAccount:
    def test_valid_withdrawal(self, everyday):
        assert everyday.withdraw(1000) is True
        assert everyday.balance == 500

    def test_maximum_withdrawal_is_enforced(self, everyday):
        assert everyday.withdraw(1001) is False
        assert everyday.balance == 1500
        assert everyday.transactions == []

    def test_card_number_is_masked(self, everyday):
        assert everyday.masked_card_number == "**** **** **** 4444"

    @pytest.mark.parametrize("card", ["1234", "abcdabcdabcdabcd", 1234])
    def test_invalid_card_number(self, card):
        account = EverydayAccount(1007, 100, card)
        assert account.masked_card_number == "No card linked"

    def test_month_end_charges_fee(self, everyday):
        assert everyday.month_end() is True
        assert everyday.balance == 1495
        assert everyday.transactions[-1].amount == 5

    def test_month_end_waives_fee_on_high_balance(self):
        account = EverydayAccount(1008, 2000, "1234123412341234")
        assert account.month_end() is False
        assert account.balance == 2000

    def test_month_end_without_funds_for_fee(self):
        account = EverydayAccount(1009, 3, "1234123412341234")
        assert account.month_end() is False
        assert account.balance == 3


class TestTransactionHistory:
    def test_records_are_kept_in_order(self, everyday_with_history):
        amounts = [r.amount for r in everyday_with_history.transactions]
        assert amounts == [100, 800, 45.50, 120]
        ids = [r.transaction_id for r in everyday_with_history.transactions]
        assert ids == [1, 2, 3, 4]

    def test_records_store_resulting_balance(self, everyday_with_history):
        last = everyday_with_history.transactions[-1]
        assert last.resulting_balance == pytest.approx(634.50)

    def test_transaction_count(self, everyday_with_history):
        assert everyday_with_history.transaction_count() == 4

    def test_transactions_of_type(self, everyday_with_history):
        withdrawals = everyday_with_history.transactions_of_type(
            "Withdrawal")
        assert [r.amount for r in withdrawals] == [800, 45.50, 120]
        assert everyday_with_history.transactions_of_type("Fee") == []

    def test_transactions_above(self, everyday_with_history):
        large = everyday_with_history.transactions_above(100)
        assert [r.amount for r in large] == [800, 120]

    def test_history_is_a_copy(self, everyday_with_history):
        everyday_with_history.transactions.clear()
        assert everyday_with_history.transaction_count() == 4

    def test_statement_lists_every_record(self, everyday_with_history):
        lines = everyday_with_history.statement().split("\n")
        assert lines[0].startswith("Statement for Everyday account 1002")
        assert len(lines) == 5
        assert "Groceries" in lines[3]

    def test_statement_with_no_history(self, savings):
        assert savings.statement().endswith("No transactions yet")