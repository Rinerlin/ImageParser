# curl  -v --request POST "http://10.0.0.14/default/en_US/send.html?type=sms" --data "u=admin&p=admin&l=1&n=89896237004m=Смс из Петухона"
import requests

# res = requests.get('https://scotch.io')
url = "http://10.0.0.14/default/en_US/send.html?type=sms"
aututl = "http://admin:admin@10.0.0.14/default/en_US/tools.html?type=sms"
post = requests.post(url,
                     data={"u": "admin", "p": "admin", "l": "1", "n": "89896237004", "m": "AAAAAAAAAAAAAAAAAAAAAAAAA"})
# r = requests.get(aututl)
print(post.text)
