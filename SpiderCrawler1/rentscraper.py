from bs4 import BeautifulSoup
import requests

def scrapedetails(link):
    session = requests.Session()
    session.headers.update({'User-Agent': 'Custom user agent'})
    html =session.get(link)
    html = html.text
    soup = BeautifulSoup(html, 'html5lib')

    price = ''
    address = ''
    furnished = ''
    type = []
    movein = ''
    extradetails = ''
    facilities = ''
    ccdistance = ''

    for tag in soup.find_all('div', {'id': 'smi-price-string'}):
        price = tag.text
    for tag in soup.find_all('div', {'class': 'smi-object-header'}):
        address = tag.find('h1').text
    for tag in soup.find_all('span', {'class': 'header_text'}):
        type.append(tag.text)
    for tag in soup.find_all('div', {'id': 'overview'}):
        furnished = tag.text
    for tag in soup.find_all('div', {'id': 'description'}):
        extradetails = tag.text
    for tag in soup.find_all('table', {'id': 'facilities'}):
        facilities = tag.text
    for tag in soup.find_all('div', {'class': 'map_info_box'}):
        ccdistance = tag.text

    return price, address, type, extradetails, furnished, facilities, ccdistance