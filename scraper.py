
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


def create_driver():
    options = Options()
    options.add_argument("--headless=new")  
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


url = "https://quotes.toscrape.com/"


driver = create_driver()
driver.get(url)
time.sleep(2)  

soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()


quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

data = []
for q, a in zip(quotes, authors):
    data.append({"Quote": q.text, "Author": a.text})


df = pd.DataFrame(data)
df.to_csv("quotes.csv", index=False, encoding="utf-8-sig")

print("✅ تم حفظ البيانات في quotes.csv")

