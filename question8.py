import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

content = soup.find(id="mw-content-text")
if content is None:
    print("Error: Could not find the content section on the page.")         # Error running code prior to adding headers variable
    exit()

headings = content.find_all("h2")

exclude_words = ["References", "External links", "See also", "Notes"]

file = open("headings.txt", "w")

for heading in headings:
    heading_text = heading.get_text(strip=True)
    heading_text = heading_text.replace("[edit]", "").strip()
    if not any(exclude_word in heading_text for exclude_word in exclude_words):
        file.write(heading_text + "\n")

file.close()