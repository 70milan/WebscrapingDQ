import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

address = "https://www.amazon.com/GLEYEMOR-Polarized-Rectangle-Sunglasses-Glasses/dp/B09WTLW8X2/?_encoding=UTF8&pd_rd_w=vrFLr&content-id=amzn1.sym.9d39c3fa-c33a-4f7a-8d61-434712e0d436&pf_rd_p=9d39c3fa-c33a-4f7a-8d61-434712e0d436&pf_rd_r=S187027ZF410HY2BV6Q6&pd_rd_wg=yokIj&pd_rd_r=018363ee-f550-4085-9f01-40bd452abd49&ref_=pd_gw_bmx_gp_20oqmewn"

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


def return_desc(address):
    # calling get method of requests library
    response = requests.get(address, headers=header_values)
    # response hasve an attri called text.encode("utf-8") to read the text.
    response_text = response.text.encode("utf-8")
    soup = BeautifulSoup(response_text, 'lxml')
    descs = soup.find_all("div", {"id": "detailBullets_feature_div"})
   
   
    #[-4].get_text().strip()
    for d in descs:
        desc = d.find("span", text= re.compile(r'B0', re.DOTALL))
       
    print(desc.text)

return_desc(address)











