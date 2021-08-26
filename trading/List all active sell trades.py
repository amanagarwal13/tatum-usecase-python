import http.client

conn = http.client.HTTPSConnection("api-eu1.tatum.io")

headers = { 'x-api-key': "8db09a7f-7b42-49e9-b40b-5f7ea1976085" }

conn.request("GET", "/v3/trade/sell?id=5e68c66581f2ee32bc354087&customerId=5e68c66581f2ee32bc354087&pageSize=10&offset=0&pair=BTC%2FEUR&count=SOME_STRING_VALUE", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))