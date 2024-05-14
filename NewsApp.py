import requests
import json


query = input("Enter the news topic : ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-05-14&sortBy=popularity&apiKey=892a9af1e0d946dc83cec5d8e901a064"

r = requests.get(url)

news = json.loads(r.text)

for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("--------------------------------------")
