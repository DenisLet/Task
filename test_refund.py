import requests
import json
from test_data import TestConfig

def perform_refund(private_key) :
    API_URL_REFUND = TestConfig.api_urls['refund']
    token, amount = TestConfig.token_amount
    payload = {
        "token" : token,
        "amount": amount
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {private_key}'
    }

    resp = requests.post(API_URL_REFUND, json=payload, headers=headers)
    resp_data = json.loads(resp.text)
    if resp.status_code == 200:

        token = resp_data['token']
        assert resp_data['success'] == True, f'{token} {resp_data["refund"]["status"]}'
    else:
        error = resp_data['errors']
        assert resp_data['success'] == True, f'Something gone  wrong: {resp.status_code} : {error}'

