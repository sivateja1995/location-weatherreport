import requests
import json

city=input('input the city name:  ')
url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=56eeb1eb05170558d1333d044c94df18&units=metric'.format(city)

res= requests.get(url)
api=json.loads(res.content)


temp=api['main']['temp']
humidity=api['main']['humidity']
wind_speed=api['wind']['speed']
description=api['weather'][0]['description']

print('temp:{} Degree Celsius'.format(temp))
print('humidity: {} %'.format(humidity))
print('wind speed: {} m/s'.format(wind_speed))
print('Description:{} '.format(description))
print()
print('--------------------')


