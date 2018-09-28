# from lxml import html
import requests 
from bs4 import BeautifulSoup
import re


class WebCrawler:
    def __init__(self, starting_url, depth):
        self.starting_url = starting_url
        self.depth=depth+1
        self.ads = set()
        self.pages= set()

    def crawl(self):
        for i in range( 1, self.depth):
            print(i)
            self.pages.add(self.starting_url+str(i))
        
        for page in self.pages:
            self.get_links(page)

        return
    
    def get_links(self, link):
        start_page = requests.get(link)
        data = start_page.text
        soup = BeautifulSoup(data)
        for link in soup.findAll('a',href=re.compile("/mieten/")):
            if  "search-resultlist-searchresultspageitem" in link.get('data-gtm-id'):
                self.ads.add("https://www.homegate.ch"+link.get('href'))
        return

    # def get_pages(self, link):
    #     start_page = requests.get(link)
    #     data = start_page.text
    #     soup = BeautifulSoup(data)
    #     for link in soup.findAll('a',href=re.compile("/mieten/")):
    #         if "search-resultlist-searchresultspagingnavigator-a-" in link.get('data-gtm-id'):
    #             print("page",link.get('href'))
    #             self.pages.add("https://www.homegate.ch"+link.get('href'))

    #     return     

class Web:
    def __init__(self, name, link):
        self.name = name
        self.link = link

    def __str__(self):
        return ("Link"+ self.name + " " +self.link)

crawler= WebCrawler('https://www.homegate.ch/mieten/immobilien/kanton-zuerich/trefferliste?ep=',50)
crawler.crawl()
print(len(crawler.ads), len(crawler.pages))
for ad in crawler.ads:
    print(ad)
    f = open("links.txt", "a")
    f.write(ad)
    f.write("\n")
