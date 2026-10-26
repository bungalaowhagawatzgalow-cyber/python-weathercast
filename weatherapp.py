import requests
from datetime import datetime
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable

def weatherfunc():
    url = "https://api.open-meteo.com/v1/forecast" # so the code actually works it takes the data from this url
    geolocator = Nominatim(user_agent="weatherapp", timeout=10)

    chosen_unit = input("Temperature unit (fahrenheit, celsius or kelvin): ").strip().lower()

    while True:

        while chosen_unit not in ("celsius", "fahrenheit", "kelvin"):
            print("Invalid unit! Please try again.")
            chosen_unit = input("Temperature unit (fahrenheit, celsius or kelvin): ").strip().lower() # in a while loop so if you write it wrong it doesnt correct you only 1 time
        else:
            break

    api_unit = "celsius" if chosen_unit == "kelvin" else chosen_unit

    params = {
        "city": input("City: "),
        "country": input("Country: "),
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation,cloud_cover",
        "timezone": "auto",
        "temperature_unit": api_unit,
        "wind_speed_unit": "kmh",
        "precipitation_unit": "mm",
    }

    location = geolocator.geocode(params["city"] + ", " + params["country"])

    if location is None: # if the place you inputted is not in their data base and will exit after 3 seconds
        print("City not found")
        print("Closing application in 3 seconds")
        time.sleep(3)
        exit()
    else:
        longitude = location.longitude
        latitude = location.latitude

    geolocation = {
        "latitude": latitude,
        "longitude": longitude,
    }

    params.update(geolocation)

    params.pop("city")
    params.pop("country")

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    weather = response.json()
    current = weather["current"]

    KELVIN = 273.15 # adds this to celsius since meteo does not have a kelvin temp unit
    kelvin = current["temperature_2m"] + KELVIN

    print("Weather showing for this time:", weather["current"]["time"])
    time.sleep(1)

    if chosen_unit == "fahrenheit":
        print("Temperature:", current["temperature_2m"], "°F")

    elif chosen_unit == "celsius":
        print("Temperature:", current["temperature_2m"], "°C")

    elif chosen_unit == "kelvin":
        print("Temperature:", kelvin, "K")

    print("Humidity:", current["relative_humidity_2m"], "%")
    print("Wind speed:", current["wind_speed_10m"], "km/h")
    print("Precipitation:", current["precipitation"], "mm")
    print("Timezone:", weather["timezone"])
    time.sleep(2)

    wannastart = input("Wanna continue? y/n: ").lower() # asks if you want to continue again

    if wannastart == "y": # if yes it will go on
        weatherfunc()
        api_unit = "celsius" if chosen_unit == "kelvin" else chosen_unit
    elif wannastart == "n": # else itll quit
        print("Closing in 3 seconds")
        time.sleep(3)
        exit()

weatherfunc() # calls the function