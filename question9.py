import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/Machine_learning"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

content = soup.find("div", {"id":"mw-content-text"})
if content is None:
    print("Error: Could not find the content section on the page.")         # Troubleshooting to find content
    exit()

tables = content.find_all("table")

data_table = None
for table in tables:
    rows = table.find_all("tr")
    if len(rows) > 3:
        data_table = table

if table is None:
    print("Error")
    exit()

header_cells = table.find_all("tr")
headers = [header.get_text(strip=True) for header in header_cells]

if not headers:
    headers = [f"col{i+1}" for i in range(len(table.find_all("tr")[1].find_all("th")))]

file = open("wiki_table.csv", "w", newline="")
writer = csv.writer(file)
writer.writerow(headers)

rows = data_table.find_all("tr")
for row in rows:
    cols = row.find_all("td")
    row_data = [col.get_text(strip=True) for col in cols]

    while len(row_data) < len(headers):
        row_data.append("")

    writer.writerow(row_data)

file.close()
