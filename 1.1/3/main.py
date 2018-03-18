# Текущий курс евро
# https://www.cbr-xml-daily.ru/daily_json.js

import urllib.request, json

data_url = 'https://www.cbr-xml-daily.ru/daily_json.js'
currency = 'EUR'
template = 'Курс {0}: {1:.2f}'

with urllib.request.urlopen(data_url) as url:
    data    = json.loads(url.read().decode())
    details = data['Valute'][currency]
    
    print(template.format(details['Name'], details['Value']))
