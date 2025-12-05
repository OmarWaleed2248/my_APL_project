# استدعاء المكتبات
import requests
from bs4 import BeautifulSoup
import pandas as pd

# رابط الموقع التجريبي
url = "https://quotes.toscrape.com/"

# جلب صفحة الموقع
response = requests.get(url)

# تحويل الصفحة ل BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# جمع الاقتباسات والمؤلفين
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

# تجهيز البيانات في قائمة
data = []
for q, a in zip(quotes, authors):
    data.append({"Quote": q.text, "Author": a.text})

# تحويل البيانات ل DataFrame وحفظها في CSV
df = pd.DataFrame(data)
df.to_csv("quotes.csv", index=False)

print("✅ تم حفظ البيانات في quotes.csv")
