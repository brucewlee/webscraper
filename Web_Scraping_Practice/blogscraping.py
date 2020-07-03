import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://webscraper.io/test-sites/e-commerce/allinone')

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all(class_='title')
prices = soup.find_all(class_='pull-right price')

for title in titles:
    title_t = title.get_text()
    print(title_t)

for price in prices:
    print(price)
