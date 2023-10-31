import http.client
import json
from test_data import TestConfig
import requests

MERCHANT_PRIVATE_KEY = 'your_merchant_private_key'
SANDBOX_URL = 'https://business.reactivepay.com'


def get_order_info(order_number):
    connection = http.client.HTTPSConnection('business.reactivepay.com')

    payload = {
        "orderNumber": order_number
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {TestConfig.private_key}'
    }

    connection.request("POST", "/api/v1/payments", json.dumps(payload), headers)

    response = connection.getresponse()
    data = response.read()

    return {
        'request': {
            'method': 'POST',
            'path': '/api/v1/payments',
            'headers': headers,
            'body': payload
        },
        'response': {
            'status': response.status,
            'reason': response.reason,
            'headers': response.getheaders(),
            'body': json.loads(data.decode('utf-8'))
        }
    }


# Пример запроса информации по order_number_1
result1 = get_order_info('order_number_1')

# Пример запроса информации по order_number_2
result2 = get_order_info('order_number_2')

# Сохранение результатов в файлы
with open('request1.txt', 'w') as file:
    file.write(json.dumps(result1, indent=4))

with open('request2.txt', 'w') as file:
    file.write(json.dumps(result2, indent=4))




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

    result = {
        'request': {
            'url': response.request.url,
            'method': response.request.method,
            'headers': dict(response.request.headers),
            'body': json.loads(response.request.body) if response.request.body else None
        },
        'response': {
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'body': json.loads(response.text) if response.text else None
        }
    }

    with open('balance_request.json', 'w') as file:
        json.dump(result, file, indent=4)

    if response.status_code == 200:
        resp_o = json.loads(response.text)
        balance = resp_o['wallet']['available']
        return balance
    else:
        return f'Something gone wrong: {response.status_code} - {response.text}'

get_balance('EUR')