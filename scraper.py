from bs4 import BeautifulSoup
import requests
from data import data_list

uri = 'https://www.marketwatch.com/tools/marketsummary'
response = requests.get(uri)
if (response.status_code != 200):
    raise Exception("Unable to access website")

soup = BeautifulSoup(response.text, 'lxml')
table = soup.find("table", id="marketsummaryindexes")

all_table_data = table.find_all("td")

for table_data in all_table_data:
    if (table_data.a):
        data_list.append(table_data.a['title'])
    else:
        data_list.append(table_data.text)


def chunks(array, length):
    for i in range(0, len(array), length):
        yield array[i:i+length]


def filter_index(index):
    index_expression = (index + 1) % 2 != 0
    if(index_expression):
        return True
    else:
        return False


grouped_data_list = list(chunks(data_list, 4))
for grouped_data in grouped_data_list:
    for index, item in enumerate(grouped_data):
        if(filter_index(index)):
            print(item)
