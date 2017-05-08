from Samples import searchengine

pagelist = ['http://www.ginkouin.com/banklist/']
#pagelist = ['http://www.whoocus.com/blog/', 'http://f-feather.com/']
crawler = searchengine.crawler('')
crawler.crawl(pagelist)
