import requests
from bs4 import BeautifulSoup
import xlwt
import pandas as pd
import re
import time
import sys
import io
import emoji
import random
def main():


    newfile = '三亚天域度假酒店.txt'

    f = open(newfile, 'w')
    headers = {
                'authority': 'www.mafengwo.cn',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
               'referer': 'https://www.mafengwo.cn/hotel/1460.html?iMddid=10030',
                 'x - requested -with': 'XMLHttpRequest',
                  'accept': 'application / json, text / javascript, * / *; q = 0.01',
             'accept - encoding': 'gzip, deflate, br',
            'accept - language': 'zh - CN, zh;q = 0.9'

    }

    num = 1
    for num in range(1, 865):
        # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
        url = 'https://www.mafengwo.cn/hotel/info/comment_list?poi_id=1460&type=0&keyword_id=0&page='+str(num)
        res = requests.get(url, headers=headers)

        soup = BeautifulSoup(res.text, 'html.parser')

        html = res.content
     #马蜂窝数据应该是加密了

        ht2 = html.decode('unicode-escape')
        # ht2 = ht1.replace('\/', '/')
        highpoints = re.compile(u'[\ud800-\uDBFF][\udC00-\udFFF]')
        ht3 = highpoints.sub(u'', ht2)
        eachcomment_list = []
        comment_list = re.findall(r'\btxt">.*?<', ht3),
        for item in comment_list:
            i = 0
            for i in range(0,10) :
                temp = item[i].lstrip('txt">').rstrip('<')
           # eachcomment_list.append(item[].lstrip('txt">').rstrip('<'))
                eachcomment_list.append(temp)

        #
        # fdataframe = pd.DataFrame(data=eachcomment_list, columns =['评论'])
        #
        # fdataframe.to_csv('reader.csv',encoding= 'utf-8', index=False, mode='a')
        # # print('已保存为cs   v文件.')
        print('存储了第'+str(num)+'页')
        for line in eachcomment_list:
         f =open(newfile, 'a')
         f.write(line+'\n')
         f.close()

        time.sleep(random.random()*3)



if __name__ == '__main__':
    main()
