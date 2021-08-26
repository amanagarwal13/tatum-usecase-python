import http.client

conn = http.client.HTTPSConnection("api-eu1.tatum.io")

payload = "{\"accounts\":[{\"currency\":\"BTC\",\"xpub\":\"xpub6EsCk1uU6cJzqvP9CdsTiJwT2rF748YkPnhv5Qo8q44DG7nn2vbyt48YRsNSUYS44jFCW9gwvD9kLQu9AuqXpTpM1c5hgg9PsuBLdeNncid\",\"customer\":{\"accountingCurrency\":\"USD\",\"customerCountry\":\"US\",\"externalId\":\"123654\",\"providerCountry\":\"US\"},\"compliant\":false,\"accountCode\":\"AC_1011_B\",\"accountingCurrency\":\"USD\",\"accountNumber\":\"123456\"}]}"

headers = {
    'content-type': "application/json",
    'x-api-key': "a25d4389-2007-4771-a42f-56ba33c71baf"
    }

conn.request("POST", "/v3/ledger/account/batch", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))