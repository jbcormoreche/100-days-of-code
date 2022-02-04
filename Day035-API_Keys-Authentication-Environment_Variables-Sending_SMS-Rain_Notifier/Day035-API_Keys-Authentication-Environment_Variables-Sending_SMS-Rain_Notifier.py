# API Keys, Authentication, Environment Variables and Sending SMS

# API authentication is used to access more secure and more valuable data from API providers
# Data can be available for free or have free and paid plans which have limits to the access provided
# An API key is used for authorization

# Environment variables allow to separate where the keys and other variables are stored from the code base
# They can be used to hide API keys, to keep them secret, for convenience and for security purposes
# You can store them as environment variables (key=value pairs)

# Check the environment variables that are set in the environment in which the code is running by typing "env" in the terminal

# Create an environment variable (in all caps)
# For example, paste "export OWP_API_KEY=69f04e4613056b159c2761a9d9e664d2" into terminal

# Day 35 Project - Rain Notifier
# Check if it will rain in the next 12 hours
import requests
import os
from twilio.rest import Client

parameters = {
    "lat": 51.507351,
    "lon": -0.127758,
    "exclude": "current,minutely,daily",
    "appid": os.environ.get("OWP_API_KEY")
}

# Environment variables would need to be created for these too
account_sid = "AC7c357bb2c70d78979800071781270f39"
auth_token = "0549b71f9a1e07f77368c2e0bacb53485"

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

next_weather = [weather_data["hourly"][i]["weather"][0]["id"] for i in range(0, 12)]
for weather_id in next_weather:
    if weather_id < 700:
        will_rain = True

# Sending an SMS
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an umbrella.",
            from_="+15017122661",
            to="+15558675310"
        )

print(message.status)
