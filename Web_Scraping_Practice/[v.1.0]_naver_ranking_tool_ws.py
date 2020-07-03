import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://search.shopping.naver.com/search/all.nhn?origQuery=%EC%86%90%EC%86%8C%EB%8F%85%EC%A0%9C&pagingIndex=5&pagingSize=40&viewType=list&sort=rel&frm=NVSHPAG&query=%EC%86%90%EC%86%8C%EB%8F%85%EC%A0%9C')

soup = BeautifulSoup(response.text, 'html.parser')

infos = soup.find_all(class_="info")

with open('results_naver.csv','w',encoding='UTF-8') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Ranking','Ad/판매처', 'Title', 'Price', 'Date', 'Review', 'Spec']
    csv_writer.writerow(headers)
    ranking = 0

    for info in infos:

        try:
            ad = info.find(class_="price").find('a', href=True).get_text()
        except:
            ad = " "

        ranking = ranking + 1

        title = info.find(class_="tit").get_text()
        title = title.replace(","," ")

        try:
            price = info.find(class_="num _price_reload").get_text()
        except:
            price = " "
        price = price.replace(","," ")

        try:
            date = info.find(class_="date").get_text()
        except:
            date = " "
        date = date.replace(","," ")

        try:
            review = info.find(class_="etc").find("a").find("em").get_text()
        except:
            review = " "

        try:
            specs = info.find(class_="detail").find("a",href=True).get_text()
        except:
            specs =" "

        specs = specs.replace(":"," ")

        csv_writer.writerow([ranking, ad, title, price, date, review, specs])
