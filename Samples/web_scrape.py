from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
from re import compile

try:
  url = urlopen('http://www.amazon.co.jp/gp/registry/wishlist/2G3O65D98BFUZ/ref=cm_wl_list_o_2?')
#  url = urlopen('http://www.whoocus.com/blog')
  html = BeautifulSoup(url.read(), 'lxml')

  print(html.title)
  print(html.title.text)
  print(html.h1)
  #print(html.h1.a['title'])

  images = html.findAll("img", {"src":compile("http://ecx.images-amazon.com/images/.*\.jpg")})
  for image in images:
    print(image['src'])

except HTTPError as err:
  print('HTTPError', err)
except URLError as err:
  print('URLError', err)
else:
  pass

