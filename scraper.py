from bs4 import BeautifulSoup
import requests
from matplotlib import pyplot
import numpy

data_list = []


def get_website(uri):
    response = requests.get(uri)
    if (response.status_code != 200):
        raise Exception("Unable to access website")
    website = BeautifulSoup(response.text, 'lxml')
    return website


def get_table_data():
    return [
        table_data.a['title'] if table_data.a else table_data.text
        for table_data in get_website("https://www.marketwatch.com/tools/marketsummary").find(
            "table", id="marketsummaryindexes").find_all("td")
    ]


def data_processor():
    data = dict()
    raw_data = get_table_data()[4:]
    for index, name in enumerate(raw_data[::4]):
        value = raw_data[index*4+2]
        data[name] = float(value.replace('+', ''))
    return data


def make_plot():
    data = data_processor()
    y_val = numpy.arange(len(names))
    pyplot.bar(y_val, data.values(), align='center')
    pyplot.xticks(y_val, data.keys(), rotation=45, ha="right")
    pyplot.ylabel('Market Movement')
    pyplot.xlabel('Market Indexes')
    pyplot.title("Market Overview")
    pyplot.show()


if __name__ == "__main__":
    make_plot()
