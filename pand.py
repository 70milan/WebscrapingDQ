import pandas as pd
import csv
  
# assign header columns
headerList = ['col1', 'col2', 'col3']
  
# open CSV file and assign header
with open("C:/projects/py/WebScrapping/csvtest/price_list_1.csv", 'w') as file:
    dw = csv.DictWriter(file, delimiter=',', 
                        fieldnames=headerList)
    dw.writeheader()
  
# display csv file
fileContent = pd.read_csv("price_list_1.csv")
fileContent
