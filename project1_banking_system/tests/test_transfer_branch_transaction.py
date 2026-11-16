"""Tests for Transfer, Branch and Transaction."""
import pytest

from banking_system.branch import Branch
from banking_system.transaction import Transaction
from banking_system.transfer import Transfer


class TestTransfer:
    def test_successful_transfer(self, everyday, savings):
        transfer = Transfer(everyday, savings, 200)
        assert transfer.execute() is True
        assert everyday.balance == 1300
        assert savings.balance == 700
        assert str(transfer).endswith("Completed")

    def test_transfer_is_recorded_on_both_accounts(self, everyday, savings):
        Transfer(everyday, savings, 200).execute()
        out = everyday.transactions[-1]
        into = savings.transactions[-1]
        assert (out.transaction_type, out.amount) == ("Withdrawal", 200)
        assert (into.transaction_type, into.amount) == ("Deposit", 200)

    def test_transfer_cannot_run_twice(self, everyday, savings):
        transfer = Transfer(everyday, savings, 200)
        transfer.execute()
        assert transfer.execute() is False
        assert savings.balance == 700

    def test_source_rules_block_transfer(self, savings, everyday):
        # Savings must keep $100, so $450 out of $500 fails.
        transfer = Transfer(savings, everyday, 450)
        assert transfer.execute() is False
        assert savings.balance == 500
        assert everyday.balance == 1500
        assert str(transfer).endswith("Failed")

    def test_same_account_is_rejected(self, savings):
        assert Transfer(savings, savings, 50).execute() is False
        assert savings.transaction_count() == 0

    def test_non_account_is_rejected(self, savings):
        assert Transfer(savings, "1002", 50).execute() is False
        assert savings.balance == 500


class TestBranch:
    def test_open_and_close(self, branch):
        assert branch.open_branch() is True
        assert branch.open_branch() is False
        assert branch.close_branch() is True
        assert branch.close_branch() is False

    def test_feedback_is_stored(self, branch):
        assert branch.add_feedback("Friendly staff") is True
        assert branch.add_feedback("   ") is False
        assert branch.feedback == ["Friendly staff"]

    def test_invalid_details_use_defaults(self):
        branch = Branch(0, "", "", 12)
        assert str(branch).startswith("Branch 0 - Unnamed branch")
        assert branch.branch_name == "Unnamed branch"
        assert branch.branch_suburb == "Unknown suburb"
        assert branch.phone_number is None

    def test_setters_validate(self, branch):
        branch.branch_name = "Glenelg"
        branch.branch_suburb = 5
        assert branch.branch_name == "Glenelg"
        assert branch.branch_suburb == "Adelaide"

    def test_str_and_repr(self, branch):
        assert str(branch) == ("Branch 1 - Adelaide CBD, Adelaide "
                               "(phone 0812345678, Closed)")
        assert repr(branch).startswith("Branch(1, 'Adelaide CBD'")


class TestTransaction:
    def test_str_and_repr(self):
        record = Transaction(3, "Withdrawal", 45.5, 954.5, "Groceries")
        assert str(record) == ("#3 Withdrawal of $45.50 (Groceries), "
                               "balance after: $954.50")
        assert repr(record) == (
            "Transaction(3, 'Withdrawal', 45.5, 954.5, 'Groceries')")


class TestExtraFixtures:
    """Tests that use the second fixture for each class."""

    def test_interest_on_minimum_balance(self, savings_at_minimum):
        assert savings_at_minimum.month_end() is True
        assert savings_at_minimum.balance == pytest.approx(103)

    def test_deposit_then_withdraw_back_to_minimum(self, savings_at_minimum):
        savings_at_minimum.deposit(50)
        assert savings_at_minimum.withdraw(50) is True
        assert savings_at_minimum.balance == 100

    def test_busy_branch_closes_and_keeps_feedback(self, busy_branch):
        assert busy_branch.close_branch() is True
        assert busy_branch.feedback == ["Friendly staff",
                                        "Long queue at lunch"]

    def test_feedback_list_is_a_copy(self, busy_branch):
        busy_branch.feedback.append("Added from outside")
        assert len(busy_branch.feedback) == 2

    def test_records_describe_themselves(self, deposit_record,
                                         withdrawal_record):
        assert str(deposit_record) == ("#1 Deposit of $250.00 (Pay), "
                                       "balance after: $750.00")
        assert withdrawal_record.transaction_type == "Withdrawal"
        assert withdrawal_record.amount == pytest.approx(45.5)

    def test_pending_transfer(self, pending_transfer, everyday, savings):
        assert str(pending_transfer).endswith("Pending")
        assert pending_transfer.execute() is True
        assert (everyday.balance, savings.balance) == (1200, 800)