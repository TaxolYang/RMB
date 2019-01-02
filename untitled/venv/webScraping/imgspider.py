import requests
from bs4 import BeautifulSoup
import os
import urllib.request
import time
import random
from random import randint

page = 4
# flag = False
newfile = '1微博.txt'
path1 = os.path.join('img', newfile)
for year in range(2018, 2015, -1):
    for month in range(5, 1, -1):


        for date in range(29, 1, -3):
            # if(flag==False):
            #     date = 19
            #     flag = True
            for page in range(1, 50):
                headers = {
                        'Host': 's.weibo.com',
                        'Referer': 'https://s.weibo.com/weibo?q=%E6%99%9A%E9%A4%90&scope=ori&haspic=1&Refer=g&page=2',
                        'Upgrade-Insecure-Requests': '1',
                        'X-Forwarded-For': str(randint(1, 255))+'.'+str(randint(1, 255))+'.'+str(randint(1, 255))+'.'+str(randint(1, 255)),
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
                        'Cookie': 'SINAGLOBAL=2600044568305.1245.1539160824221; wvr=6; login_sid_t=b1b63e219239bb04d97ad717edab9a5a; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; UOR=www.google.com.hk,www.weibo.com,www.baidu.com; Apache=1688769208254.0684.1540131589071; ULV=1540131589076:4:4:1:1688769208254.0684.1540131589071:1540013657357; SCF=Ai0mrAZ6Bw5_8HL3FhzKIPa6Q8DxOuSm4CT5YQECs-uMPciKlAeLXrLtUT__kYg-C1wOWUSMO_sDvxzVTOhOUpc.; SUHB=0S7Db9R6h1S4P6; WBStorage=e8781eb7dee3fd7f|undefined; WBtopGlobal_register_version=a6a3e8a5473574f8'
                    }
                url ='https://s.weibo.com/weibo?q=晚餐&scope=ori&haspic=1&timescope=custom::'+str(year)+'-'+str(month)+'-'+str(date)+'&Refer=g&page='+str(page)

                res = requests.get(url, headers=headers)
                soup = BeautifulSoup(res.content, 'html.parser')

                soup.encode('utf-8')
                name_list = []
                text_list = []
                img_link = []

                img_link = soup.select('.m3 > li > img')


                for i in img_link:
                    url1 ='https:'+i['src'].replace('thumb150', 'bmiddle')
                    imgname_list = url1.split('/')
                    filename =imgname_list.pop()
                    path = os.path.join('img', filename)

                    urllib.request.urlretrieve(url1, filename=path)
                    print('正在存取%s-%s-%s第%s页'%(year, month, date, page)+str(i))



                    # time.sleep(random.random()*3)



                i = 0

                # for i in range(20):
                #     text_list.append(soup.select('.txt')[i].text)
                # f = open(path1, 'w')
                # for line in text_list:
                #     f = open(path1, 'a', encoding='utf-8')
                #
                #     try:
                #         f.write(line.strip()+'\n')
                #     except Exception as ex:
                #         print(ex.message)
                #     print('正在打印第'+str(page))
                #
                #
                #     f.close()
                #
                #     time.sleep(random.random()*3)
