import requests
import json
from bs4 import BeautifulSoup


res = requests.get('http://bonze.tw')
soup = BeautifulSoup(res.text, "html.parser")

obj =  {}
obj['article'] = []
# json.dumps

for drink in soup.select('.article-field.title'):
    addItem = {'title': drink.get_text(),'href' : drink.find('a').get('href')}
    obj['article'].append(addItem)

# print(drink.get_text())
# print(drink.prettify())
print (obj)


with open('bonze.json', 'w') as f:
     json.dump(obj,f,ensure_ascii=False,sort_keys = True ,indent = 4)
