import json
import requests

city_name = 'Madrid'
key = '2f44ab8d94825710392977b37c24d3ac'
response = requests.post(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}')
result = json.loads(response.text)
print(result)
