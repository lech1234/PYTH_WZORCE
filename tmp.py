x = {
  "table": "A",
  "currency": "dolar amerykański",
  "code": "USD",
  "rates": [
    {
      "no": "054/A/NBP/2023",
      "effectiveDate": "2023-03-17",
      "mid": 4.4202
    }
  ]
}
import requests
r = requests.get('https://api.nbp.pl/api/exchangerates/rates/a/usd/?format=json')
print(r.status_code)
r.raise_for_status()
j = r.json()
print(j['rates'][0]['mid'])
import datetime as dt
d1 = dt.date.today()
td1 = dt.timedelta(days=1)
d2 = d1 - 365 * td1
print(d2)