from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

def getInternalLinks(bsObj, includeUrl):
  print("getInternalLinks")

def getExternalLinks(bsObj, excludeUrl):
  print("getExternalLinks")

def getRandomExternalLinks(startingPage):
  print("getRandomExternalLinks")

def followExternalOnly(startingSite):
  print("followExternalOnly")
  externalLink = getRandomExternalLinks(startingSite)

followExternalOnly("http://oreilly.com")