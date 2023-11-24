from datetime import datetime
import rentscraper
import rentlinkspider
import sqlite3

def run_daft_rentspider():
    st = datetime.now()
    daftstr = 'https://www.daft.ie'
    links = rentlinkspider.crawl_links()
    i = 1
    db = sqlite3.connect('dafthouses.db')
    cursor = db.cursor()
    cursor.execute('DELETE FROM rentcurrenttable')
    print(links)
    print(datetime.now())
    for link in links:

        link = daftstr+''.join(link)
        data = rentscraper.scrapedetails(link)

        houseinfo = {
            'price': data[0],
            'address':data[1],
            'type':data[2],
            'details':data[3],
            'furnished': data[4],
            'facilities':data[5],
            'ccdistance':data[6],
        }
        print(type(houseinfo['price']))
        print(type(houseinfo['address']))
        typestr ="".join( houseinfo['type'])
        print(type(houseinfo['details']))
        print(type(houseinfo['furnished']))
        print(type(houseinfo['ccdistance']))
        print(type(houseinfo['facilities']))
        print(houseinfo['ccdistance'])
        print(houseinfo['facilities'])
        newstr = houseinfo['facilities'].replace("/", "")
        keys = houseinfo.keys()

        cursor.execute('''INSERT INTO rentcurrenttable(price,address,type,details,furnished,facilities,ccdistance)
                          VALUES(?,?,?,?,?,?,?)''', (houseinfo['price'], houseinfo['address'], typestr,
                                                     houseinfo['details'], houseinfo['furnished'],
                                                     newstr, houseinfo['ccdistance']))

        print('House' + str(i) + 'Inserted')
        i += 1
        db.commit()

    print('alan')
    #tablescleaner.addtofulltables()
    print('Total download and databsase addition time:')
    print(datetime.now() - st)