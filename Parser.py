import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import Main


def getImageFromURL(url):
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    vacancies_names = soup.find_all('div', class_='story-image__content')
    imageTable = []
    for name in vacancies_names:
        a = name.a['href']
        if ".jpg" in a:
            imageTable.append(name.a['href'])
            # print(name.a['href'])
    return imageTable


def getAndDownImage(url, n):
    import urllib.request
    urllib.request.urlretrieve(url, f"{n}.jpg")


AllURL = getImageFromURL("https://pikabu.ru/story/v_rossii_sozdali_shmel_analog_britanskogo_mikrobespilotnika_black_hornet_9927759")
n = 0
for i in AllURL:
    getAndDownImage(i, n)
    n += 1
