import http.client

conn = http.client.HTTPSConnection("api-eu1.tatum.io")

headers = { 'x-api-key': "a25d4389-2007-4771-a42f-56ba33c71baf" }

conn.request("GET", "/v3/ledger/account?pageSize=10&offset=0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))