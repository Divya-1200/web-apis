import requests, json

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

CITY = "Hyderabad"
API_KEY = "12b9af6c1daea22bfdb6e498a60f9e17"

URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

response = requests.get(URL)

if response.status_code == 200:
   
   data = response.json()

   print(data)
  
   main = data['main']
  
   temperature = main['temp']
  
   humidity = main['humidity']
   
   pressure = main['pressure']
 
   report = data['weather']
   print(f"{CITY:-^30}")
   print(f"Temperature: {temperature}")
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Weather Report: {report[0]['description']}")
else:
   # showing the error message
   print("Error in the HTTP request")
