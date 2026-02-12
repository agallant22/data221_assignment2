import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

page_title = soup.find("title").get_text()
print("Page Title: ", page_title)

content_div = soup.find("div", id = "mw-content-text")

paragraphs = content_div.find_all("p")
for p in paragraphs:
    text = p.get_text(strip=True)
    if len(text) >= 50:
        print(text)
        break