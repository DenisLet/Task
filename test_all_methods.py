from test_payments import perform_payment
from test_payout import perform_payout
from test_refund import perform_refund
from test_data import TestConfig
import pytest



@pytest.mark.payment  # pytest -vvv -k payment
@pytest.mark.parametrize("currency", TestConfig.currencies)
@pytest.mark.parametrize("amount", TestConfig.success_amounts + TestConfig.fail_amounts)
def test_payments(currency, amount):
    perform_payment(TestConfig.private_key, currency, amount)


@pytest.mark.payout   # pytest -vvv -k payout
@pytest.mark.parametrize("currency", TestConfig.currencies)
@pytest.mark.parametrize("amount", TestConfig.success_amounts + TestConfig.fail_amounts)
def test_payouts(currency, amount):
    perform_payout(TestConfig.private_key, currency, amount)


@pytest.mark.refund   # pytest -vvv -k refund
def test_refund():
    perform_refund(TestConfig.private_key)