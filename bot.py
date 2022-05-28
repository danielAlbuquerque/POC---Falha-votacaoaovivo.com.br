import requests

import random
from bs4 import BeautifulSoup as bs
import traceback
import json


def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # request and grab content
    soup = bs(requests.get(url).content, 'html.parser')
    # to store proxies
    proxies = []
    for row in soup.find("table", attrs={"class": "table-striped"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            proxies.append(str(ip) + ":" + str(port))
        except IndexError:
            print('error')
            continue
    return proxies

url = "https://www.eleicoesaovivo.com.br/alizee.php"
proxies = get_free_proxies()
# proxies = [ "186.248.89.6:5005" ]
headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
data = { 'dk': '11', 'vr': '175', 'vy': 'dsadsar', 'nm': '13' }

for i in range(len(proxies)):

    #printing req number
    print("Request Number : " + str(i+1))
    proxy = proxies[i]

    try:
        print(proxy)
        response = requests.post(url, data = data, headers=headers, timeout=60, proxies = {"http":proxy, "https":proxy})
        print(response.text)
    except:
        # if the proxy Ip is pre occupied
        print("Not Available")