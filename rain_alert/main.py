import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "Your API Key"
account_sid = "Your account sid"
auth_token = "Your AUTH TOKEN"

weather_parameter = {
    "lat": "Your latitude",
    "lon": "Your Longitude",
    "appid": api_key,
    "exclude": "current,minutely,daily"

}


response = requests.get(OWN_ENDPOINT, params=weather_parameter)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]


will_rain = False


for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True


if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}


    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages \
        .create(
        body="หากจะออกไปข้างนอก อย่าลืมนำร่มไปด้วยนะคะ ☔️",
        from_='Your Phone Number Twilio',
        to='Your phone number send to'
    )

    print(message.status)




