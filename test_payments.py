import requests
import json
import pytest
import logging
from test_data import TestConfig

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def perform_payment(private_key, currency, amount):
    API_URL_PAYMENT = TestConfig.api_urls['payment']

    payload = {
        "product": "Your Product Name",
        "amount": amount,
        "currency": currency,
        "redirectSuccessUrl": "http://www.example.com/success",
        "redirectFailUrl": "http://www.example.com/fail",
        "extraReturnParam": "Your Order No",
        "orderNumber": "Your Order Number",
        "locale": "en"
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {private_key}'
    }

    response = requests.post(API_URL_PAYMENT, json=payload, headers=headers)

    resp_payload = json.loads(response.text)

    if response.status_code == 200:
        token = resp_payload['token']
        current_status = resp_payload["payment"]["status"]
        success = resp_payload['success']
        logging.info(f'Payment of {amount} in {currency} was successful. Status: {current_status}')
        assert success == True, f'Payment of {amount} in {currency} failed. Status: {current_status}'
    else:
        current_status = f'{resp_payload["errors"]}'
        logging.error(f'Payment of {amount} in {currency} failed. Error code: {response.status_code}. Status: {current_status}')
        assert success == True, f'Payment of {amount} in {currency} failed. Error code: {response.status_code}. Status: {current_status}'
