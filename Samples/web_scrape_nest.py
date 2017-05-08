from urllib.request import urlopen
from urllib.parse import unquote
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
  global pages
  # url = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
  # url = urlopen('https://ja.wikipedia.org/wiki/%E7%B6%BE%E7%80%AC%E3%81%AF%E3%82%8B%E3%81%8B')
  url = urlopen('https://ja.wikipedia.org/' + pageUrl)
  html = BeautifulSoup(url.read(), 'lxml')

  for link in html.findAll("a", href=re.compile("^(/wiki/)")):
    #    for link in html.find('div', {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
      if link.attrs['href'] not in pages:
        newPage = link.attrs['href']
        print(unquote(newPage))
        pages.add(newPage)
        getLinks(newPage)
#      else:
#        print(unquote(link.attrs['href']))

getLinks('')
