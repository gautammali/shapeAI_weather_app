import requests
from datetime import datetime

api_key = '68c63b569f5b4859185a160d2349bef5'
location = input("Enter the place: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
humi = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("Weather Stats for - {}  || {}".format(location.upper(), date_time))

print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc  :", weather_desc)
print("Current Humidity      :", humi, '%')
print("Current wind speed    :", wind_spd, 'kmp/h')
r=requests.get(complete_api_link)
with open('weather.txt','w') as f:
    f.write(r.text)
