
import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

data = []
for q, a in zip(quotes, authors):
    data.append({"Quote": q.text, "Author": a.text})

df = pd.DataFrame(data)
df.to_csv("quotes.csv", index=False)

print("✅ تم حفظ البيانات في quotes.csv")

