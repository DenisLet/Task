
import os

class TestConfig:
    # private_key = 'baa2920a5b90e8a445d4'
    api_urls = {
        'payment': 'https://business.reactivepay.com/api/v1/payments',
        'payout': 'https://business.reactivepay.com/api/v1/payouts',
        'refund': 'https://business.reactivepay.com/api/v1/refunds'
    }

    token_amount = (
        'qjuG44ngw6ARqMfWWjmys5iuLvLo8yac',
        100
    )

    currencies = ['EUR', 'USD', 'RUB']
    success_amounts = [1, 100, 987654321]
    fail_amounts = [-1, 0.01, 77**55]

