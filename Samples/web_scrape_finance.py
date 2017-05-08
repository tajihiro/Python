from urllib.request import urlopen
from urllib.parse import unquote
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = urlopen('http://stocks.finance.yahoo.co.jp/stocks/detail/?code=4281.T')
    html = BeautifulSoup(url.read(), 'lxml')
    price = html.findAll('td', {"class":"stoksPrice"})

    print(price[1].contents[0])