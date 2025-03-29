import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self,
                 site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup (html, parser)
        z = sp.find_all("a")
        print(z)
        for tag in z:
            url = tag.get("href")
            print(url)
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)

news = "https://news.google.com/"
Scraper(news).scrape()