import requests

headers = {
    'x-api-key': 'a25d4389-2007-4771-a42f-56ba33c71baf',
    'Content-Type': 'application/json',
}

data = '{ "currency": "BTC", "accountingCurrency": "EUR", "customer": { "externalId": "SERVICE_CUSTOMER_EXTERNAL_ID" } }'

response = requests.post('https://api-eu1.tatum.io/v3/ledger/account', headers=headers, data=data)
print(response.text)