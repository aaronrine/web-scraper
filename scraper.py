from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.marketwatch.com/tools/marketsummary').text
soup = BeautifulSoup(html, 'lxml')
table = soup.find("table", id="marketsummaryindexes")

head = table.find("th")

table_data = table.find_all("td")
for raw_table_data in table_data:
    if(raw_table_data.a):
        processed_table_data = raw_table_data.a.text
    else:
        processed_table_data = raw_table_data.text
    print(processed_table_data)
