import requests
from bs4 import BeautifulSoup
import html5lib

url = 'https://www.moneycontrol.com/commodity/gold-price.html#05feb2020'

headers = {"User-agents" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content,'html5lib')
price = soup.find(class_="gr_30").get_text().strip()
new_price = float(price)

print("Now Gold Price In India Is",new_price)