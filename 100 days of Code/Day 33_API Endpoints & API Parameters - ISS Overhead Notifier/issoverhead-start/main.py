from os import makedirs
import requests
from datetime import datetime
import smtplib
from math import fabs
import time

my_lat = 21.239470
my_long = 106.091600

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if fabs(iss_latitude-my_lat) < 5 and fabs(iss_longitude-my_long) < 5:
        return True


def is_night():
    parameters = {
        "lat": my_lat,
        "lng": my_long,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if sunset<=time_now.hour or sunrise>=time_now.hour:
        return True

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login("ndh2912001@gmail.com", "0987941901")
            connection.sendmail(
                from_addr="ndh2912001@gmail.com",
                to_addrs="ndh2912001@gmail.com",
                msg="Subject:Hey, ISS is close to your position!\n\nLook up it"
            )
    time.sleep(10)

