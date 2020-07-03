from bs4 import BeautifulSoup

import index

soup = BeautifulSoup(index.html_doc, 'html.parser')

#Direct
#print(soup.head.title)
"""
el = soup.find('div')
find_all()
el = soup.find_all('div')
el = soup.find_all('div')[1]
el = soup.select('#section-1')

get_text()
"""
el = soup.find()
print(el)
