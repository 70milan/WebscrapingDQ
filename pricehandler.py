from bs4 import BeautifulSoup
import requests
import config

def return_price(address):
    # calling get method of requests library
    response = requests.get(address, headers=config.header_values)
    # response hasve an attri called text.encode("utf-8") to read the text.
    response_text = response.text.encode("utf-8")
    soup = BeautifulSoup(response_text, 'lxml')
    price = soup.find("span", {"class": "a-offscreen"}).text
    return price

