def getAndDownImage(url):
    import urllib.request
    urllib.request.urlretrieve(url, "C:/Users/User/Desktop/local-filename.jpg")

linksList = ['https://cs13.pikabu.ru/post_img/big/2023/02/06/5/167566349414985569.png',
          'https://cs14.pikabu.ru/post_img/big/2023/02/06/5/1675663511133162338.png',
          'https://cs13.pikabu.ru/post_img/big/2023/02/06/5/1675663536170810257.png',
          'https://cs13.pikabu.ru/post_img/big/2023/02/06/5/1675663563199061094.png',
          'https://cs13.pikabu.ru/post_img/big/2023/02/06/5/1675663566151092369.png',
          'https://cs14.pikabu.ru/post_img/big/2023/02/06/5/167566356414573110.png',
          'https://cs13.pikabu.ru/post_img/big/2023/02/06/5/167566356811412573.png']
print(linksList[3])

getAndDownImage(linksList[0])