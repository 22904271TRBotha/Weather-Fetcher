#imports of API
import requests

#imports for text-to-speech
import pyttsx3

language = 'en'

API_KEY = "e1d842f14f046d6110526d88a733788d"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print("Weather is going to be: ", weather)
    temperature = round(data["main"]["temp"] - 273.15, 1)
    print("Average Temperature is: ", temperature)

    engine = pyttsx3.init()

    ttsText = city + "'s weather is " + weather + ", and the average temperature is " + str(temperature) + " degrees celcius."

    engine.say(ttsText)
    engine.runAndWait()
else:
    print("An error occurred.")