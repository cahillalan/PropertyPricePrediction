from bs4 import BeautifulSoup
import requests
from datetime import datetime

def twentylinks(link):
    session = requests.Session()
    session.headers.update({'User-Agent': 'Custom user agent'})
    html =session.get(link)
    html = html.text
    soup = BeautifulSoup(html, 'html5lib')
    headers = soup('h2')
    links = []
    for i in headers:
        for a in i.find_all('a',href=True):
            links.append(a['href'])

    nextlink = soup('li',{'class':'next_page'})

    nextpage = []
    for li in nextlink:
        nextpage.append(li.a['href'])

    return links,nextpage