"""Tests for Client and its dictionary of accounts."""
import pytest

from banking_system.client import Client
from banking_system.everyday_account import EverydayAccount
from banking_system.finance_exceptions import AccountNotFoundError
from banking_system.savings_account import SavingsAccount


class TestClientDetails:
    def test_invalid_details_use_defaults(self):
        client = Client("", 0, 12)
        assert client.client_id == 0
        assert client.client_name == "Unknown"
        assert client.phone_number is None

    def test_phone_number_setter_validates(self, client):
        client.phone_number = 498765432
        client.phone_number = 12345
        assert client.phone_number == 498765432

    def test_client_name_setter_validates(self, client):
        client.client_name = "   "
        assert client.client_name == "Alice Smith"

    def test_str_and_repr(self, client_with_accounts):
        assert str(client_with_accounts).endswith("2 account(s))")
        assert repr(client_with_accounts).startswith("Client('Alice Smith'")


class TestAccountDictionary:
    def test_accounts_are_keyed_by_number(
        self, client_with_accounts, savings, everyday
    ):
        assert client_with_accounts.accounts == {1001: savings,
                                                 1002: everyday}

    def test_get_account_returns_the_same_object(
        self, client_with_accounts, savings
    ):
        assert client_with_accounts.get_account(1001) is savings

    def test_get_missing_account_raises(self, client_with_accounts):
        with pytest.raises(AccountNotFoundError, match="9999") as info:
            client_with_accounts.get_account(9999)
        assert info.value.client_id == 123456789

    def test_has_account(self, client_with_accounts):
        assert client_with_accounts.has_account(1002)
        assert not client_with_accounts.has_account(9999)

    def test_duplicate_account_number_is_rejected(self, client_with_accounts):
        copy = SavingsAccount(1001, 50, 0.01)
        assert client_with_accounts.add_account(copy) is False
        assert client_with_accounts.get_account(1001).balance == 500

    def test_non_account_is_rejected(self, client):
        assert client.add_account("1001") is False
        assert client.accounts == {}

    def test_accounts_dictionary_is_a_copy(self, client_with_accounts):
        client_with_accounts.accounts.clear()
        assert len(client_with_accounts.accounts) == 2

    def test_remove_account_by_number(self, client_with_accounts, everyday):
        assert client_with_accounts.remove_account(1002) is True
        assert not client_with_accounts.has_account(1002)
        # The account is unlinked, not destroyed.
        assert everyday.balance == 1500

    def test_remove_missing_account(self, client_with_accounts):
        assert client_with_accounts.remove_account(9999) is False
        assert len(client_with_accounts.accounts) == 2

    def test_total_balance(self, client_with_accounts):
        assert client_with_accounts.total_balance() == 2000


class TestClientAccountInteractions:
    def test_operations_on_retrieved_account(self, client_with_accounts):
        account = client_with_accounts.get_account(1002)
        account.deposit(500)
        account.withdraw(200, "Bills")
        assert client_with_accounts.total_balance() == 2300
        assert account.transaction_count() == 2

    @pytest.mark.parametrize("acc_number", [1001, 1002])
    def test_both_types_managed_the_same_way(
        self, client_with_accounts, acc_number
    ):
        # No type checks: every account answers the same calls.
        account = client_with_accounts.get_account(acc_number)
        assert account.deposit(100) is True
        assert account.withdraw(50) is True
        assert account.transaction_count() == 2

    def test_specialised_rules_are_handled(self, client_with_accounts):
        assert client_with_accounts.withdraw_from(1001, 450) is False
        assert client_with_accounts.withdraw_from(1002, 1200) is False
        assert client_with_accounts.total_balance() == 2000

    def test_withdraw_from_and_deposit_to(self, client_with_accounts):
        assert client_with_accounts.withdraw_from(1002, 200, "Bills")
        assert client_with_accounts.deposit_to(1001, 50)
        assert client_with_accounts.total_balance() == 1850

    def test_missing_account_is_handled(self, client_with_accounts):
        assert client_with_accounts.deposit_to(9999, 100) is False
        assert client_with_accounts.withdraw_from(9999, 100) is False
        assert len(client_with_accounts.accounts) == 2

    def test_refused_operation_keeps_history(self, client_with_accounts):
        everyday = client_with_accounts.get_account(1002)
        everyday.deposit(10)
        client_with_accounts.withdraw_from(1002, 1001)
        client_with_accounts.deposit_to(1002, "ten")
        assert everyday.transaction_count() == 1

    def test_month_end_handles_failed_fee(self, client):
        client.add_account(EverydayAccount(1011, 2, "1234123412341234"))
        assert client.month_end() == {1011: False}
        assert client.get_account(1011).balance == 2

    def test_month_end_runs_for_every_account(self, client_with_accounts):
        results = client_with_accounts.month_end()
        assert results == {1001: True, 1002: True}
        assert client_with_accounts.total_balance() == pytest.approx(
            512.50 + 1495)

    def test_month_end_reports_waived_fee(self, client):
        client.add_account(EverydayAccount(1010, 5000, "1234123412341234"))
        assert client.month_end() == {1010: False}

    def test_preferred_branch(self, client, branch):
        client.preferred_branch = branch
        client.preferred_branch = "Glenelg"
        assert client.preferred_branch is branch