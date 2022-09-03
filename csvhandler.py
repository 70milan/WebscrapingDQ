import csv

def writetocsv(values, filename):
    csvfile = open(filename, "a", encoding="utf-8", newline="") #create a new file if it doesnt exist and (w-->write; a-->open/create and write)
    writer = csv.writer(csvfile) #writer from csv lib and pass the csvfile. once we hav ethat we can call writerow function and pass price and finally closing the file
    writer.writerow(values) # the value will be splitted by default (₹,3,3,8,.,0,0) therefore [] should be used to treat it as a single object.
    csvfile.close