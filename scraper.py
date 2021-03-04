from bs4 import BeautifulSoup
import requests

uri = 'https://www.marketwatch.com/tools/marketsummary'
response = requests.get(uri)
if (response.status_code != 200):
  raise Exception("Unable to access website")

soup = BeautifulSoup(response.text, 'lxml')
table = soup.find("table", id="marketsummaryindexes")

all_table_data = table.find_all("td")
for table_data in all_table_data:
    if (table_data.a):
        table_data = table_data.a
    print(table_data.text)
