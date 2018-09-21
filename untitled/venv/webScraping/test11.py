#计算运行时间
import datetime
starttime = datetime.datetime.now()
#引入相关库
from selenium import webdriver
from bs4 import BeautifulSoup
import time
#导入Keys 模块[键盘]
from selenium.webdriver.common.keys import Keys
import csv
#主体部分
url = 'http://hotels.ctrip.com/hotel/5311088.html?isFull=F#ctm_ref=hod_sr_lst_dl_n_1_2'
browser = webdriver.Chrome('E:/chromedriver.exe')
browser.get(url) #打开网页
page = 1
with open('file.csv','w',encoding = 'utf-8') as f:
    while page < 5:
        html = browser.page_source
        body = BeautifulSoup(html,"html.parser")
        user_list = body.find('div',{"class":"comment_detail_list"})
        #print(user_list)
        name_counter = 0
        for user_info in user_list:
            n = page *(name_counter+1)
            print('第{}页第{}个用户'.format(page,name_counter+1))
            #获取用户名
            user_name = user_info.find('p',{"class":"name"}).find('span')
            if user_name is None:
                user_name = None
            else:
                user_name = user_name
            #print(user_name.get_text())
                        #保存结果
            f.write("{}\n".format(user_name))
            name_counter +=1  
        print(name_counter)
        print('____________________-')
        page +=1
        obj = page
        time.sleep(8)
        #执行翻页操作,搜索框输入页码
        input = browser.find_element_by_xpath("//input[@id='cPageNum']")
        input.clear()
        input.send_keys(obj)
        input.send_keys(Keys.ENTER)
       #以上各项指标比较粗糙，因为担心html的<a><div>等组件存在差异【其实，我看了一些确实有差异，所以才改成粗糙的获取方式；注释掉的print括号内有些可能不正确，我也每检查，反正后来不需要了。replace,strip等方法可以让结果去除掉无用字符

#获取结束时间
#long running
endtime = datetime.datetime.now()
print (endtime - starttime).seconds
