import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

class crawler:
    def __init__(self, dbname):
        pass

    def __del__(self):
        pass

    def dbcommit(self):
        pass

    def getentryid(self, table,field,value,createnew=True):
        return None

    def addtoindex(self,url,soup):
        print('Indexing %s' % url)

    def gettextonly(self, soup):
        return None

    def separatewords(self, text):
        return None

    def isindexed(self, url):
        return False

    def addlinkref(self, urlFrom, urlTo, linkText):
        pass

    def crawl(self, pages, depth=1):
        for i in range(depth):
            newpages = set()
            for page in pages:
                try:
                    response = urllib.request.urlopen(page)
                except:
                    print('Could not open %s' % page)
                    continue
                soup = BeautifulSoup(response.read(),'lxml')
                self.addtoindex(page, soup)

                links = soup('a')
                for link in links:
                    if('href' in dict(link.attrs)):
                        url = urllib.parse.urljoin(page, link['href'])
                        print(url)

    def createindextables(self):
        pass

