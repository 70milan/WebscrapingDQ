from turtle import title
import config
import datetime
import csvhandler as ch
import pricehandler as ph
import os
import config
import title as t
import pandas as pd



date_stamp = datetime.datetime.now().date()
time_stamp = datetime.datetime.now().time()
price = ph.return_price(config.address)
title = t.return_title(config.address)

file_name = "price_list_1.csv"

abs_file_path = os.path.join(r'C:/projects/py/WebScrapping/csvtest', file_name)

row_to_write = [date_stamp, time_stamp, price,title]

ch.writetocsv(row_to_write,abs_file_path)



'''<Response [200]> # successfull
<Response [400]> # bad request
<Response [503]> server error for all code in 500 range : the reason for its failure is because header is missing and the get request only sends browrsers body.
Beautifusoup lib is needed to parse and query different elements from the incomming html. bs4 is needed since module name is bs4
1) pass variable as arg and also need to provide a parser
2) find method of soup class: using this method to find price of the item. this method takes two
args, span and its criteria [key/value pair].
3) importing csv to sav ethis in csv

'''
