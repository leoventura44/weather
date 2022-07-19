import requests
from pprint import pprint

API_Key = '98390ce78bbfa458f6434f4c180a5ec1'

city = input('Digite o nome de uma cidade: ')

base_url = 'http://api.openweathermap.org/data/2.5/weather?appid='+API_Key+'&q='+city

weather_data = requests.get(base_url).json()

pprint(weather_data)



