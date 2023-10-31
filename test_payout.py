import requests
import json
import pytest
# import logging
from test_data import TestConfig


def perform_payout(private_key, amount, currency):
    API_URL_PAYOUT = TestConfig.api_urls['payout']

    payload = {
        "amount": amount,
        "currency": currency,
        "orderNumber": "10001",
        "card": {
            "pan": "4276111152393643",
            "expires": "08/2022"
        },
        "customer": {
            "email": "test@reactivepay.com",
            "address": "test test",
            "ip": "1.1.1.1"
        }
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {private_key}'
    }

    resp = requests.post(API_URL_PAYOUT, json=payload, headers=headers)
    resp_data = json.loads(resp.text)
    if resp.status_code == 200:
        token = resp_data['payout']['token']
        print(token)
        assert resp_data['success'] == True, f'{token} {resp_data["payout"]["status"]}'
    else:
        assert resp_data['success'] == True, f'Something gone wrong: {resp.status_code} : {resp.text}'