# API Calls, Endpoints and Parameters

# API (Application Programming Interface)
# A set of commands, functions, protocols and objects to create software or interact with an external system

# An API Endpoint is the location where the data is stored

# Making API Calls
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)

# Build a Kanye West Quotes App using the Kanye West Rest API
import requests
import tkinter as tk


def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(quote_text, text=data["quote"])


window = tk.Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=300, height=414)
background_img = tk.PhotoImage(file="./Day033-API_Endpoints_Parameters-ISS_Overhead_Notifier/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 25, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = tk.PhotoImage(file="./Day033-API_Endpoints_Parameters-ISS_Overhead_Notifier/kanye.png")
kanye_button = tk.Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()

# Day 33 Project - ISS Overhead Notifier
import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351
MY_LONG = -0.127758
my_email = "test@hotmail.fr"
password = "password"


def iss_is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if iss_latitude >= MY_LAT-5 and iss_latitude <= MY_LAT+5 and iss_longitude >= MY_LONG-5 and iss_longitude <= MY_LONG+5:
        return True


# API Parameters
# Options that can be passed with the endpoint to influence the response
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset and time_now <= sunrise:
        return True


# Check every 60 seconds while the program is running
while True:
    time.sleep(60)
    if iss_is_overhead() and is_night():
        with smtplib.SMTP("smtp.live.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addr="test@gmail.com",
                msg="Subject:Look up!\n\nThe ISS is above you in the sky."
            )
