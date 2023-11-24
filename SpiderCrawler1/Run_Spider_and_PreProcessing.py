import daftspider
import daftrentspider
import DataCleaner
import CSVSplitter
import DublinDataMaker
import tablescleaner
import CorkDataMaker
import tablecreaters

daftspider.run_spider()
daftrentspider.run_daft_rentspider()
tablescleaner.addtofulltables()
DataCleaner.create_csvs()
CSVSplitter.splitCSV()
dubhouses = DublinDataMaker.createDublin15()
DublinDataMaker.googlecode(dubhouses)

corkhouses = CorkDataMaker.createCorkCity()
CorkDataMaker.googlecode(corkhouses)