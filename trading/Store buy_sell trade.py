import http.client

conn = http.client.HTTPSConnection("api-eu1.tatum.io")

payload = "{\"type\":\"BUY\",\"price\":\"8650.4\",\"amount\":\"15000\",\"pair\":\"BTC/EUR\",\"currency1AccountId\":\"7c21ed165e294db78b95f0f1\",\"currency2AccountId\":\"7c21ed165e294db78b95f0f1\",\"feeAccountId\":\"7c21ed165e294db78b95f0f1\",\"fee\":1.5,\"attr\":{\"sealDate\":1572031674384,\"percentBlock\":1.5,\"percentPenalty\":1.5}}"

headers = {
    'content-type': "application/json",
    'x-api-key': "8db09a7f-7b42-49e9-b40b-5f7ea1976085"
    }

conn.request("POST", "/v3/trade", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))