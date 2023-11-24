from datetime import datetime
import salesscraper
import linkspider
import sqlite3
import tablescleaner


def run_spider():
    st = datetime.now()
    daftstr = 'https://www.daft.ie'
    # the links in daft.ie are dynamic. ie. they are internal links that dont contain the https
    # this needs to be added if a link is to be opened
    links = linkspider.crawl_links()
    # this assigns the links to the links variable.
    # these links are retrieved by the crawllinks function
    i = 1
    db = sqlite3.connect('dafthouses.db')
    cursor = db.cursor()
    cursor.execute('DELETE FROM currenthouses')
    # remove all values from the current houses table
    print(datetime.now())
    for link in links:

        # appends the daftstring 'htts' etc to the dynamic link
        link = daftstr+''.join(link)
        data = salesscraper.scrapedetails(link)
        houseinfo = {
            'price': data[0],
            'address':data[1],
            'bedrooms':data[2],
            'bathrooms':data[3],
            'type' : data[4].split('|',1)[0],
            'details':data[5],
            'views': data[6],
            'all_prices':data[7],
            'price_dates':data[8],
            'area' : data[9]
        }

        keys = houseinfo.keys()

        # convert data to a list of dicts
        #send data to the database

        cursor.execute('''INSERT INTO currenthouses(price,address,bedrooms,bathrooms,type,details,views,allprices,pricedates,area)
                          VALUES(?,?,?,?,?,?,?,?,?,?)''', (houseinfo['price'],houseinfo['address'],houseinfo['bedrooms'],
                                                           houseinfo['bathrooms'], houseinfo['type'],
                                                           houseinfo['details'], houseinfo['views'],
                                                           houseinfo['all_prices'],houseinfo['price_dates'],
                                                           houseinfo['area']))

        i +=1
        db.commit()

    #tablescleaner.addtofulltables()
    print('Total download and databsase addition time:')
    print(datetime.now() - st)