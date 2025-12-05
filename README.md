#Web Scraping Quotes Project

This is a simple **Web Scraping** project made using **Python**, **Requests**, **BeautifulSoup**, and **Pandas**.  
The script collects quotes and their authors from the website:

🔗 https://quotes.toscrape.com/

---

## 📌 Project Description

The script sends a request to the website, extracts:
- Quote text  
- Author name  

Then saves the collected data into a CSV file called **quotes.csv**.

---

  Technologies Used
- Python
- Requests
- BeautifulSoup (bs4)
- Pandas

---

##  Files in the Project
- `scraper.py` → Main Python script for scraping data  
- `quotes.csv` → The exported data (created automatically)
- `README.md` → Project documentation

---

## ▶️ How to Run the Project

1. Install required libraries:
   ```bash
   pip install requests beautifulsoup4 pandas

   out put examples 
   | Quote                                | Author          |
| ------------------------------------ | --------------- |
| "The world as we have created it..." | Albert Einstein |
| "It is our choices..."               | J.K. Rowling    |

