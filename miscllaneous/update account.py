import http.client

conn = http.client.HTTPSConnection("api-eu1.tatum.io")

payload = "{\"accountCode\":\"AC_1011_B\",\"accountNumber\":\"123456\"}"

headers = {
    'content-type': "application/json",
    'x-api-key': "a25d4389-2007-4771-a42f-56ba33c71baf"
    }

conn.request("PUT", "/v3/ledger/account/611f926b32339342ba045366", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))