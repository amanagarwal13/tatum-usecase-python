import http.client

conn = http.client.HTTPSConnection("api-eu1.tatum.io")

headers = { 'x-api-key': "8db09a7f-7b42-49e9-b40b-5f7ea1976085" }

conn.request("GET", "/v3/bitcoin/wallet?mnemonic=SOME_STRING_VALUE", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))