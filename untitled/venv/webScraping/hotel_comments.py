import requests
from bs4 import BeautifulSoup
import time
import random
import os
from xlwt import *
newfile = '酒店评论.txt'
path = '/Users/yangxiaoyu/Desktop/'+newfile
f = open(path, 'w')
i = 0
eachcomment_list = []
while i < 3:
    url_i = 'http://hotels.ctrip.com/hotel/dianping/2895314_p'+str(i)+'t0.html'
    res = requests.get(url_i)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    comment_list = soup.find_all('div', class_='comment_txt')
    for item in comment_list:
        if item.find_all('span', class_='J_commentDetail')[0].string is not None:
          eachcomment_list.append(item.find_all('span', class_='J_commentDetail')[0].string)

    for line in eachcomment_list:
        f =open(path, 'a')
        f.write(line+'\n')
        f.close()
    i = i+20
    time.sleep(random.random()*3)


