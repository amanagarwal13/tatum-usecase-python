import http.client

conn = http.client.HTTPSConnection("api-eu1.tatum.io")

headers = { 'x-api-key': "8db09a7f-7b42-49e9-b40b-5f7ea1976085" }

conn.request("GET", "/v3/trade/history?id=5e68c66581f2ee32bc354087&pair=BTC%2FETH&pair=BTC%2FEUR&pageSize=10&offset=0&count=SOME_STRING_VALUE", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))