import http.client

conn = http.client.HTTPSConnection("api-eu1.tatum.io")

headers = { 'x-api-key': "8db09a7f-7b42-49e9-b40b-5f7ea1976085" }

conn.request("GET", "/v3/ledger/account/611f926b32339342ba045366/balance", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))