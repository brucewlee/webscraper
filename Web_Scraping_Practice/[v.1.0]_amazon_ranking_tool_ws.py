import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.amazon.com/s?k=hand+sanitizer&ref=nb_sb_noss_2')

soup = BeautifulSoup(response.text, 'html.parser')

infos = soup.find_all(class_="s-expand-height s-include-content-margin s-border-bottom s-latency-cf-section")

with open('results_amazon.csv', 'w', encoding='UTF-8') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Ranking','Title','Price']
    csv_writer.writerow(headers)
    ranking = 0

    for info in infos:

        title = info.find(class_="a-size-mini a-spacing-none a-color-base s-line-clamp-4").find("font").get_text()

        title = title.replace(","," ")

        ranking = ranking + 1

        csv_writer.writerow([ranking,title])
