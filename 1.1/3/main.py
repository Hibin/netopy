# Текущий курс евро
# https://www.cbr-xml-daily.ru/daily_json.js

import urllib.request, json 

data_url = 'https://www.cbr-xml-daily.ru/daily_json.js'
currency = 'EUR'

with urllib.request.urlopen(data_url) as url:
    data    = json.loads(url.read().decode())
    details = data['Valute'][currency]
    
    print('Курс ', details['Name'], ': ', details['Value'], sep = '')
