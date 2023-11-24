from bs4 import BeautifulSoup
import requests
from datetime import datetime
import re

def scrapedetails(link):
    session = requests.Session()

    session.headers.update({'User-Agent': 'Custom user agent'})
    # user agen as per daft.ie requirments
    html =session.get(link)
    # get the html from the link and convert it to text

    html = html.text
    soup = BeautifulSoup(html, 'html5lib')
    # then convert it to beautiful soup

    price = ''
    address = ''
    bedrooms = ''
    bathrooms =''
    house_type = ''
    extradetails = ''
    dateentered = ''
    price_history = ''
    dates_listed = ''
    meters = ''


    # use the researched tags to retrieve the information that id needed from the beautiful soup instance
    for strong_tag in soup.find_all('strong', {'class': 'PropertyInformationCommonStyles__costAmountCopy'}):
        price = strong_tag.text
    for tag in soup.find_all('h1', {'class': 'PropertyMainInformation__address'}):
        address = tag.text
    for tag in soup.find_all('div', {'class': 'QuickPropertyDetails__iconCopy'}):
        bedrooms = tag.text
    for tag in soup.find_all('div', {'class': 'QuickPropertyDetails__iconCopy--WithBorder'}):
        bathrooms = tag.text
    for tag in soup.find_all('div', {'class': 'QuickPropertyDetails__propertyType'}):
        house_type = tag.text
    for tag in soup.find_all('p', {'class': 'PropertyDescription__propertyDescription '
                                            'is-expandable PropertyDescription__propertyDescription--'
                                            'is-collasped'}):
        extradetails = tag.text
    for tag in soup.find_all('div', {'class': 'PropertyStatistics__iconData'}):
        dateentered = tag.text
    for tag in soup.find_all('div', {'class': 'PropertyPriceHistory__propertyPrice'}):
        price_history = tag.text
    for tag in soup.find_all('div', {'class': 'PropertyPriceHistory__propertyPriceDate'}):
        dates_listed = tag.text
    for tag in soup.find_all('div', {'class': 'PropertyOverview__propertyOverviewDetails'}):
        overview_details = tag.text
        meters = re.findall('\d+',overview_details)
    if meters:
        area = meters[0]
    else:
        area = 0



    return price,address,bedrooms,bathrooms,house_type,extradetails,dateentered,price_history,dates_listed,area
