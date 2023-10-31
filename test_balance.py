import requests
import json
from test_data import TestConfig

def get_balance(currency):
    MERCHANT_PRIVATE_KEY = TestConfig.private_key
    SANDBOX_URL = 'https://business.reactivepay.com'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {MERCHANT_PRIVATE_KEY}'
    }

    params = {
        'currency': currency
    }

    response = requests.get(f'{SANDBOX_URL}/api/v1/balance', params=params, headers=headers)

    if response.status_code == 200:

        resp_o = json.loads(response.text)
        balance = resp_o['wallet']['available']
        return balance
    else:
        return f'Something gone wrong: {response.status_code} - {response.text}'
