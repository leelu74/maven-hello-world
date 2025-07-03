import requests

API_KEY = os.environ.get("API_KEY") # Replace with your OpenWeatherMap API key

# List of major towns/cities in Chittoor district
places = [
    "Chittoor,IN",
    "Tirupati,IN",
    "Madanapalle,IN",
    "Punganur,IN",
    "Palamaner,IN",
    "Pileru,IN",
    "Nagari,IN"
]

weather_data = []

for place in places:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        weather_data.append((place.split(',')[0], temp))
    else:
        print(f"Could not get weather for {place}")

# Sort by temperature descending
weather_data.sort(key=lambda x: x[1], reverse=True)

print("Weather in Chittoor District (Top Temperatures):")
for name, temp in weather_data:
    print(f"{name}: {temp}°C")