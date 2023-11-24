from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime
import re

def scrapedetails():
    session = requests.Session()

    session.headers.update({'User-Agent': 'Custom user agent'})
    html =session.get('https://en.wikipedia.org/wiki/List_of_towns_in_the_Republic_of_Ireland/2002_Census_Records')
    html = html.text
    soup = BeautifulSoup(html, 'html5lib')


    my_data = []

    for tr in soup.find_all('tr'):
        my_data.append(tr.text)


    print(my_data)
    return my_data

def clean_data(mydata):

    mylist = []
    for town in mydata:
        mytown = re.search('\\n(.*),', town)
        if mytown: mylist.append(mytown.group(1))
    print(mylist)
    return mylist

def scrapestreetdetails():
    session = requests.Session()

    session.headers.update({'User-Agent': 'Custom user agent'})
    html =session.get('https://en.wikipedia.org/wiki/List_of_streets_and_squares_in_Dublin')
    html = html.text
    soup = BeautifulSoup(html, 'html5lib')


    my_data = []

    for tr in soup.find_all('tr'):
        my_data.append(tr.text)

    print(my_data)
    return my_data

def clean_streetdata(mydata):

    mylist = []
    for town in mydata:
        mytown = re.search('\\n(.*)\\n', town)
        if mytown: mylist.append(mytown.group(1))
    print(mylist)
    return mylist


clean_streetdata(scrapestreetdetails())

