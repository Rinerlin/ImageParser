import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL_TEMPLATE = "https://pikabu.ru/story/vsratyie_animemyi_403133_9915842"
r = requests.get(URL_TEMPLATE)
print(r.status_code)
#print(r.text)
soup = bs(r.text, "html.parser")
vacancies_names = soup.find_all('div', class_='story-image__content')
print(vacancies_names)
for name in vacancies_names:
    print(name.a['href'])