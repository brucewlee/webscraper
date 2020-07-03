import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.amazon.co.jp/s?k=hand+sanitizer&i=hpc&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=2LDQ56Y8IDPTL&sprefix=hand+sani%2Caps%2C350&ref=nb_sb_ss_c_2_9')

soup = BeautifulSoup(response.text, 'html.parser')

infos = soup.find_all(class_="s-expand-height s-include-content-margin s-border-bottom s-latency-cf-section")

with open('results_amazonjp.csv', 'w', encoding='UTF-8') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Ranking','Title','Price']
    csv_writer.writerow(headers)
    ranking = 0

    for info in infos:

        title = info.find(class_="a-section a-spacing-none a-spacing-top-small").find("font").get_text()
        title = title.replace(","," ")

        ranking = ranking + 1

        csv_writer.writerow([ranking,title])
