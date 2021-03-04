from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.marketwatch.com/tools/marketsummary').text
soup = BeautifulSoup(html, 'lxml')
table = soup.find("table", id="marketsummaryindexes")

all_table_data = table.find_all("td")
for table_data in all_table_data:
    if (table_data.a):
        table_data = table_data.a
    print(table_data.text)
