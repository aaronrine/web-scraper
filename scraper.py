from bs4 import BeautifulSoup
import requests
from matplotlib import pyplot
import numpy

data_list = []


def get_response(uri):
    response = requests.get(uri)
    if (response.status_code != 200):
        raise Exception("Unable to access website")
    return response


def get_website():
    raw_website = get_response(
        'https://www.marketwatch.com/tools/marketsummary').text
    website = BeautifulSoup(raw_website, 'lxml')
    return website


def set_table_data():
    all_table_data = get_website().find(
        "table", id="marketsummaryindexes").find_all("td")

    for table_data in all_table_data:
        data_list.append(table_data.a['title']) if table_data.a else data_list.append(
            table_data.text)


def data_processor():
    set_table_data()

    def chunks(array, length):
        for i in range(0, len(array), length):
            yield array[i:i+length]

    grouped_data_list = list(chunks(data_list, 4))

    data = dict()
    for grouped_data in grouped_data_list[1:]:
        name, value = grouped_data[::2]
        data[name] = float(value.replace('+', ''))
    return data


def make_plot():
    data = data_processor()
    names = list(data.keys())
    movement = list(data.values())
    y_val = numpy.arange(len(names))
    pyplot.bar(y_val, movement, align='center')
    pyplot.xticks(y_val, names, rotation=45, ha="right")
    pyplot.ylabel('Market Movement')
    pyplot.xlabel('Market Indexes')
    pyplot.title("Market Overview")
    pyplot.show()


make_plot()
