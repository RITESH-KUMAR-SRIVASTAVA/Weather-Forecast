import requests
from plyer import notification

# 1. Get coordinates from city name
city = "Delhi"
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = {"name": city, "count": 1}

try:
    geo_res = requests.get(geo_url, params=geo_params).json()
except requests.RequestException as e:
    print(f"Error fetching geocoding data: {e}")
    exit(1)

if "results" in geo_res:
    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    # 2. Get weather data
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    try:
        weather_res = requests.get(weather_url, params=weather_params).json()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        exit(1)

    if "current_weather" in weather_res:
        temp = weather_res["current_weather"]["temperature"]
        wind = weather_res["current_weather"]["windspeed"]
        weather_info = f"{city}: {temp}°C, Wind {wind} km/h"

        print("Weather:", weather_info)

        # 3. Cross-platform notification (gracefully handle missing backend)
        try:
            notification.notify(
                title="Weather Update",
                message=weather_info,
                timeout=5
            )
        except Exception:
            print("(Desktop notification unavailable — install pyobjus on macOS or notify2 on Linux)")
    else:
        print("Weather data not found")
else:
    print("City not found")
