import requests
import json
from bs4 import BeautifulSoup


res = requests.get('http://bonze.tw')
soup = BeautifulSoup(res.text, "html.parser")

obj =  []

for drink in soup.select('.article-field.title'):
    obj.append(drink.get_text())

# print(drink.get_text())
# print(drink.prettify())
print (obj)


with open('bonze.json', 'w') as f:
     json.dump(obj,f,ensure_ascii=False)
