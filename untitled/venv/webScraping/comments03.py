import requests
from bs4 import BeautifulSoup
import time
import random
import os
newfile = '肖申克的救赎评论.txt'
path = '/Users/yangxiaoyu/Desktop/'+newfile
f = open(path, 'w')
i = 0
eachcomment_list = []
while i < 237540:
    url_i = 'https://movie.douban.com/subject/1292052/comments?start='+str(i)+'&limit=20&sort=new_score&status=P'
    res = requests.get(url_i)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    comment_list = soup.find_all('div', class_='comment-item')
    for item in comment_list:
        if item.find_all('span', class_='short')[0].string is not None:
          eachcomment_list.append(item.find_all('span', class_='short')[0].string)

    for line in eachcomment_list:
        f =open(path, 'a')
        f.write(line+'\n')
        f.close()
    i = i+20
    time.sleep(random.random()*3)

print(eachcomment_list)
