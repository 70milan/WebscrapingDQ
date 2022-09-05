import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd


#######################################################################################################
address = "https://www.amazon.com/Fitness-Labs-Creapure-Creatine-Capsules/dp/B008KMUGK4/ref=dp_fod_3?pd_rd_i=B008KMUGK4&psc=1"

#needs in a dict format (key value pairs)
header_values = {

    'Accept':	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Encoding': 	'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 	'keep-alive',
    # no need to specify 'Host ':	'www.amazon.com',
    'Referer': 	'https://www.google.com/',
    'Upgrade-Insecure-Requests': 	'1',
    'User-Agent':	'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'

}
#######################################################################################################



def return_price(address):
    # calling get method of requests library
    response = requests.get(address, headers=header_values)
    # response hasve an attri called text.encode("utf-8") to read the text.
    response_text = response.text.encode("utf-8")
    soup = BeautifulSoup(response_text, 'lxml')
    price = soup.find("span", {"class": "a-offscreen"}).text
    return price

def return_desc(address):
    # calling get method of requests library
    response = requests.get(address, headers=header_values)
    # response hasve an attri called text.encode("utf-8") to read the text.
    response_text = response.text.encode("utf-8")
    soup = BeautifulSoup(response_text, 'lxml')
    descs = soup.find_all("div", {"id": "detailBullets_feature_div"})
    #[-4].get_text().strip()
    for d in descs:
        desc = d.find_all("span")[-1].get_text()
       
    return desc
#######################################################################################################


def return_cat(address):
    # calling get method of requests library
    response = requests.get(address, headers=header_values)
    # response hasve an attri called text.encode("utf-8") to read the text.
    response_text = response.text.encode("utf-8")
    soup = BeautifulSoup(response_text, 'lxml')
    cat = soup.find("span", {"class": "a-list-item"}).text.strip()
    return cat



def return_ratings(address):
    # calling get method of requests library
    response = requests.get(address, headers=header_values)
    # response hasve an attri called text.encode("utf-8") to read the text.
    response_text = response.text.encode("utf-8")
    soup = BeautifulSoup(response_text, 'lxml')
    ratings = soup.find("span", {"class": "a-icon-alt"}).text
    return ratings

#######################################################################################################
def return_title(address):
    # calling get method of requests library
    response = requests.get(address, headers=header_values)
    # response hasve an attri called text.encode("utf-8") to read the text.
    response_text = response.text.encode("utf-8")
    soup = BeautifulSoup(response_text, 'lxml')
    title = soup.find("title").text.strip()
    return title

#######################################################################################################

date_stamp = datetime.datetime.now().date()
time_stamp = datetime.datetime.now().time()
price = return_price(address)
title = return_title(address)
ratings = return_ratings(address)
cat = return_cat(address)
desc = return_desc(address)

df = pd.DataFrame([[date_stamp,time_stamp,cat,title,price,desc,ratings]], columns=['date','time','category','title','price','ASIN','ratings'])

