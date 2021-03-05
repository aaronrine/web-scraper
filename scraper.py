from bs4 import BeautifulSoup
import requests
from matplotlib import pyplot
import numpy

data_list = []
name_list = []
value_list = []

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


def coordinated_pop(array1, array2, index):
    array1.pop(index)
    array2.pop(index)


grouped_data_list = list(chunks(data_list, 4))
for grouped_data in grouped_data_list:
    for index, item in enumerate(grouped_data):
        if (index == 0):
            name_list.append(item)
        elif (index == 2):
            if('+' in item):
                cleaned_item = item.replace('+', '')
                value_list.append(float(cleaned_item))
            else:
                value_list.append(float(item))

coordinated_pop(name_list, value_list, 0)
names = name_list
y_val = numpy.arange(len(names))
movement = value_list
pyplot.bar(y_val, movement, align='center')
pyplot.xticks(y_val, names, rotation=45, ha="right")
pyplot.ylabel('Market Movement')
pyplot.xlabel('Market Indexes')
pyplot.title("Market Overview")

pyplot.show()
