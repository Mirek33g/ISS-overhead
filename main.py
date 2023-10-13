import requests
from datetime import datetime
import smtplib

MY_LAT = 53.480759  # latitude
MY_LONG = -2.242631  # longitude
MY_EMAIL = "first.steps.coding@gmail.com"
MY_PASSWORD = ""  #password

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json",
                        params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds


# Checked if the ISS is close and notify user by sending email
if iss_latitude > MY_LAT - 5 and iss_latitude < MY_LAT + 5:
  if iss_longitude > MY_LONG - 5 and iss_longitude < MY_LONG + 5:
    if time_now.hour > sunrise or time_now.hour < sunset:
      connection = smtplib.SMTP("smtp.gmail.com")
      connection.starttls()
      connection.login(user=MY_EMAIL, password=MY_PASSWORD)
      connection.sendmail(
          from_addr=MY_EMAIL,
          to_addrs="mirek.forx@gmail.com",
          msg="Subject: Look Up!\n\nThe ISS is close to your current position."
      )
      connection.close()
else:
  print("Not yet")





