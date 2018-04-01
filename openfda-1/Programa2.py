import http.client
import json

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection("api.fda.gov")
conn.request("GET", "/drug/label.json?limit=10", None, headers)
r1 = conn.getresponse()
print(r1.status, r1.reason)
drugs_raw = r1.read().decode("utf-8")
conn.close()

info = json.loads(drugs_raw)

for i in range(len(info['results'])):
    medicamento = info['results'][i]
    print("Id del medicamento: ", medicamento['id'])
