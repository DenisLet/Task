import requests
import json

def perform_payment(private_key, currency, amount):
    YOUR_SERVER_URL = 'http://localhost:5000/callback'
    API_URL_PAYMENT = 'https://business.reactivepay.com/api/v1/payments'

    payload = {
        "product": "Your Product Name",
        "amount": amount,
        "currency": currency,
        "callbackUrl": YOUR_SERVER_URL,
        "locale": "en"
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {private_key}'
    }

    response = requests.post(API_URL_PAYMENT, json=payload, headers=headers)
    resp_payload = json.loads(response.text)
    print(resp_payload)

if __name__ == '__main__':
    from test_data import TestConfig

    perform_payment(TestConfig.private_key, 'EUR', 1000)


