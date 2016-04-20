from urllib.request import urlopen
from urllib.parse import unquote
from bs4 import BeautifulSoup
import re

#url = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
url = urlopen('https://ja.wikipedia.org/wiki/%E7%B6%BE%E7%80%AC%E3%81%AF%E3%82%8B%E3%81%8B')
html = BeautifulSoup(url.read(), 'lxml')

for link in html.find('div', {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(unquote(link.attrs['href']))

