from bs4 import BeautifulSoup
import requests
from datetime import datetime
import rentlinkgatherer


def crawl_links():
    st = datetime.now()
    daftstr = 'https://www.daft.ie'
    alllinks = []
    link = rentlinkgatherer.twentylinks('https://www.daft.ie/ireland/residential-property-for-rent/?ad_type=rental&advanced=1&s%5Badvanced%5D=1&searchSource=rental')
    for i in link[0]: alllinks.append(i)
    while link[1]:
        nextlink = daftstr+''.join(link[1])
        link = rentlinkgatherer.twentylinks(nextlink)
        print(link[1])
        for i in link[0]: alllinks.append(i)
        print(len(alllinks))

    print(datetime.now()-st)
    return alllinks

