import urllib.request
import json
import pprint

APIKEY = 'c357f16e0d81f0c07549edfe15c68fd5'
city = 'Wellesley'
country_code = 'us'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'

#print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
pprint.pprint(response_data)

# Can you get the current temperature in Wellesley?
pprint.pprint(response_data['main']['temp'])
