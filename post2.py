# curl  -v --request POST "http://10.0.0.14/default/en_US/send.html?type=sms" --data "u=admin&p=admin&l=1&n=89896237004m=Смс из Петухона"
import requests

# res = requests.get('https://scotch.io')
defUrl = "http://10.0.0.14/default/en_US/status.html"
shortUrl = "http://10.0.0.14"
url = "http://10.0.0.14/default/en_US/send.html?type=sms"
autUrl = "http://admin:admin@10.0.0.14/default/en_US/tools.html?type=sms"
post = requests.post(autUrl, auth=('admin', "admin"))
# r = requests.get(aututl)
print(post.text)
