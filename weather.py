import requests

def get_weather(city):
    api_key = "b7d082249f651ee2aaf66c21c0344b45"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Complete API URL
    url = f"{base_url}?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != "404":
            main = data["main"]
            weather_description = data["weather"][0]["description"]
            temperature = main["temp"]
            humidity = main["humidity"]
            wind_speed = data["wind"]["speed"]

            weather_info = (f"Weather in {city}:\n"
                            f"Temperature: {temperature}°C\n"
                            f"Humidity: {humidity}%\n"
                            f"Wind Speed: {wind_speed} m/s\n"
                            f"Description: {weather_description.capitalize()}")
            
            return weather_info
        else:
            return f"City '{city}' not found. Please check the spelling."
    except Exception as e:
        return f"Error fetching weather data: {e}"

# print(get_weather("Kanpur"))