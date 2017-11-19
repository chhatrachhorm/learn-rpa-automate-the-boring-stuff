#! python3
# program to load current weather from api
# via cmd
# display for today and the next two days
# to run: currentWeather location
import json
import requests
import sys

if len(sys.argv) < 2:
    print('More argument pls')
    sys.exit()
location = ' '.join(sys.argv[1:])
key = 'f573d7d4988e314d3a5b85e4437dc9f5'
# download
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s' % (location, key)
print(url)
try:
    res = requests.get(url)
    res.raise_for_status()

    weatherData = json.loads(res.text)
    print(weatherData)
    w = weatherData['list']
    print('Current Weather', w)
except Exception as e:
    print(e)
