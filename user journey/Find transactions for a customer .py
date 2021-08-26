import http.client

conn = http.client.HTTPSConnection("api-eu1.tatum.io")

payload = "{\"id\":\"5e6be8e9e6aa436299950c41\",\"account\":\"5e6be8e9e6aa436299950c41\",\"counterAccount\":\"5e6be8e9e6aa436299950c41\",\"currency\":\"BTC\",\"from\":1571833231000,\"to\":1571833231000,\"amount\":[{\"op\":\"gte\",\"value\":\"1.5\"}],\"currencies\":[\"BTC\"],\"transactionType\":\"FAILED\",\"transactionTypes\":[\"CREDIT_PAYMENT\"],\"opType\":\"PAYMENT\",\"transactionCode\":\"1_01_EXTERNAL_CODE\",\"paymentId\":\"65426\",\"recipientNote\":\"65426\",\"senderNote\":\"65426\"}"

headers = {
    'content-type': "application/json",
    'x-api-key': "8db09a7f-7b42-49e9-b40b-5f7ea1976085"
    }

conn.request("POST", "/v3/ledger/transaction/customer?pageSize=10&offset=0&count=SOME_STRING_VALUE", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))