import requests, json
from decouple import config

BASE_URL = "https://newsapi.org/v2/everything?"

NEWS = "amazon"
API_KEY = config('API_KEY')
print(API_KEY)

def get_news():
   URL = BASE_URL + "q=" + NEWS + "&apiKey=" + API_KEY
   print(URL)

   response = requests.get(URL)

   if response.status_code == 200:
      
      data = response.json()

      print(data)

   else:

      print("Error in the HTTP request")

if __name__ == "__main__":
   get_news()