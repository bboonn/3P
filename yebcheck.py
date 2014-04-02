# -*- coding:utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup 

# url_YEB_bk = 'http://www.thfund.com.cn/column.dohsmode=searchtopic&pageno=0&channelid=2&categoryid=2435&childcategoryid=2436.htm#goto'

url_YEB = 'http://www.thfund.com.cn/website/funds/fundnet.jsp?fundcode=000198&amp;channelid=2&amp;categoryid=2435&amp;childcategoryid=2438&amp;pageno=0'

def makeSoup(_url):
    _headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8) AppleWebKit/535.6.2 (KHTML, like Gecko) Version/5.2 Safari/535.6.2', 
        'CacheControl': 'no-cache',
        }  
    req = urllib.request.Request(
        url = _url,    
        headers = _headers  
        )  
    response = urllib.request.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html)
    return soup


def removeElement(list, _element):
    while _element in list:
        list.remove(_element)

def main():
    soup_YEB = makeSoup(url_YEB)
    # info_YEB = soup_YEB.body.find("table", attrs={"class": "huibao"}).get_text('|', strip=True)
    info_ = soup_YEB.body.find("table", attrs={"style" : "margin-left:10px;font-size:12px;"}).find("tr").find_next_siblings("tr", limit=8)
    info_YEB = ""
    for k in info_:
        info_YEB += k.get_text()

    info_YEB = info_YEB.split('\n')

    removeElement(info_YEB, '')

    info_key_YEB = info_YEB[0:3]
    info_value_YEB = []

    for i in range(3, len(info_YEB), 3):
        info_value_YEB.append(info_YEB[i:i+3])

    
    print('\n' + '余额宝近七日单位收益情况:')
    print('-='*25 + '\n' + '|'.join(info_key_YEB))
    
    for res in info_value_YEB:
        print('|'.join(res) + '\n')
    
    
    # del soup_YEB
    
if __name__ == "__main__":
    main()
