import sqlite3

def create_rent_current():
    db = sqlite3.connect('dafthouses.db')

    cursor = db.cursor()
    cursor.execute('''
           CREATE TABLE if not exists rentcurrenttable(id INTEGER PRIMARY KEY, price TEXT,
                              address TEXT, type TEXT , 
                              details TEXT, furnished TEXT,
                               facilities TEXT, ccdistance TEXT)
       ''')
    db.commit()

def create_rent_main():
    db = sqlite3.connect('dafthouses.db')

    cursor = db.cursor()
    cursor.execute('''
           CREATE TABLE if not exists rentmaintable(id INTEGER PRIMARY KEY, price TEXT,
                              address TEXT, type TEXT , 
                              details TEXT, furnished TEXT,
                               facilities TEXT, ccdistance TEXT)
       ''')
    db.commit()


def create_no_duplicates():
    db = sqlite3.connect('dafthouses.db')

    cursor = db.cursor()
    cursor.execute('''
           CREATE TABLE if not exists mainhousestable(id INTEGER PRIMARY KEY, price TEXT,
                              address TEXT, bedrooms INTEGER , 
                              bathrooms INTEGER, type TEXT,
                               details TEXT, views INTEGER,
                               allprices TEXT, pricedates TEXT,
                                area INTEGER)
       ''')
    db.commit()

def create_viable():
    db = sqlite3.connect('dafthouses.db')

    cursor = db.cursor()
    cursor.execute('''
           CREATE TABLE if not exists viablehousestable(id INTEGER PRIMARY KEY, price INTEGER,
                              address TEXT, bedrooms INTEGER , 
                              bathrooms INTEGER, type TEXT,
                               details TEXT, views INTEGER,
                               allprices TEXT, pricedates TEXT,
                                area INTEGER)
       ''')
    db.commit()
def create_current():
    db = sqlite3.connect('dafthouses.db')

    cursor = db.cursor()
    cursor.execute('''
           CREATE TABLE if not exists currenthousestable(id INTEGER PRIMARY KEY, price INTEGER,
                              address TEXT, bedrooms INTEGER , 
                              bathrooms INTEGER, type TEXT,
                               details TEXT, views INTEGER,
                               allprices TEXT, pricedates TEXT,
                                area INTEGER)
       ''')
    db.commit()

create_rent_main()
create_rent_current()
create_current()
create_no_duplicates()
create_viable()