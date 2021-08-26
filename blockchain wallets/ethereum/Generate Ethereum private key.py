import http.client

conn = http.client.HTTPSConnection("api-eu1.tatum.io")

payload = "{\"index\":0,\"mnemonic\":\"urge pulp usage sister evidence arrest palm math please chief egg abuse\"}"

headers = {
    'content-type': "application/json",
    'x-testnet-type': "SOME_STRING_VALUE",
    'x-api-key': "8db09a7f-7b42-49e9-b40b-5f7ea1976085"
    }

conn.request("POST", "/v3/ethereum/wallet/priv", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))