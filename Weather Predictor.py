import requests

def get_weather_forecast(city):
    # Pro-tip: Keep your API keys in environment variables for better security!
    api_key = "b584d2a7bb544f2aa2985427260505"

    # FIX 1: Corrected the spelling of "forecast" in the URL
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=1&aqi=no&alerts=no"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            location = data['location']['name']
            country = data['location']['country']
            temp = data['current']['temp_c']
            condition = data['current']['condition']['text']

            # Shorthand for readability
            day_data = data['forecast']['forecastday'][0]['day']

            max_temp = day_data['maxtemp_c']
            min_temp = day_data['mintemp_c']

            # FIX 2: Corrected "forcastday" to "forecastday" (API standard)
            chance_of_rain = day_data['daily_chance_of_rain']

            print(f"\n-- Weather Report for {location}, {country} --")
            print(f"Current Temp: {temp}°C")
            print(f"Predicted Max: {max_temp}°C")
            print(f"Predicted Min: {min_temp}°C")
            print(f"Condition: {condition}")
            print(f"Chance of rain: {chance_of_rain}%")

            if chance_of_rain > 50:
                print("Advice: You should probably stay inside or bring an umbrella!")
            else:
                print("Advice: It looks like a clear day ahead.")
        else:
            print(f"Error: {response.status_code}. Could not find city.")

    except Exception as e:
        print(f"An error has occurred: {e}")

city_input = input("What is your city? ")
get_weather_forecast(city_input)