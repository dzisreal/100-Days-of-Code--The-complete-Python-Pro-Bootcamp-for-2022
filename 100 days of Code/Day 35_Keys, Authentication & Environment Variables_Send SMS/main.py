import requests

OWM_Endpoint = "http://api.openweathermap.org/data/2.5/onecall"
api_key = "5e62e2cc2c6a62267935ff2eac0f0827"


weather_params = {
    "lat":21.262541,
    "lon":106.098358,
    "appid":api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
weather_data =  response.json()
weather_slice = weather_data["hourly"][:12]

for hour_data in weather_slice:
    print(hour_data["weather"][0]["description"])