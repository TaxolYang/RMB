import requests
from bs4 import BeautifulSoup
import time
import random
import os
from xlwt import *
headers = {


    'Referer': 'https://www.mafengwo.cn/hotel/40046.html?iMddid=10065',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'

}
url = 'https://www.mafengwo.cn/hotel/info/comment_list?poi_id=40046&type=0&keyword_id=0&page=2'
res = requests.get(url, headers=headers)
soup =BeautifulSoup(res.text, 'html.parser')
print(soup.text)
