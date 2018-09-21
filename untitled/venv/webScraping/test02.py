# /*!
#  * sinaadToolkit.Media
#  * @author acelan<xiaobin8[at]staff.sina.com.cn> zhouyi<zhouyi3[at]staff.sina.com.cn>
#  * @version 1.0.0
#  *
#  *                          $$!   ;$;
#  *                    !$  $$$$  !$$$   ;;
#  *                 $ *$$;$$$$$$$$$$;*$$$
#  *                $$$$$$$$$$$$$$$$$$$$$
#  *               $$$$$$;         o$$$$$o
#  *              *$$$   *#####;     $$$$$
#  *              $$$   &#$*!###     $$$$!
#  *              $$$;  $#!!###$   ;$$$$
#  *                $$$o  ;**   !$$$$!
#  *          !$&&&&$!  o$$$$$$o;   ;$&###&!     ;o$&&##&$;
#  *       ###########$ o####*  #############!  o############
#  *     ;#####;        #####  $####    *####;          ####*
#  *      ###########  o####   ####;    ####$  $######;o####
#  *          ;*#####o ####$  ####&    !#### o####     ####
#  *    ####$**&####$ ;####  o####     ####o &####$o$#####
#  *   ;o########$    *###   ####!    &####   ;######&!
#  *                 ###;
#  *                  ##o
#  *                 ;#!
#  *                 ;
#  */



import requests
from datetime import datetime
from bs4 import BeautifulSoup
url = 'http://news.sina.com.cn/o/2018-09-12/doc-ihiycyfx9732896.shtml'
res = requests.get(url)
res.encoding = 'utf-8'
# print(res.text)
soup = BeautifulSoup(res.text, "html.parser")
# print(soup)
title = soup.select('.main-title')
time = soup.select('.date-source')
print(title[0].text)
timesource = (soup.select('.date-source')[0].contents[1]).text
print(type(timesource))#timesource 是str字符串类型
timesource = datetime.strptime(timesource, '%Y年%m月%d日 %H:%M')
print(type(timesource))#timesource通过datetime转换成datetime类型。
print((time[0].contents[1]).text)
print((time[0].contents[3]).text)
article = []
text = soup.select('#article p')[:-1]
print(type(text))
print(text)
for p in text:
    article.append(p.text.strip())
# print(article)
'@'.join(article)
print(article)
