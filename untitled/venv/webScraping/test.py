import requests
from bs4 import BeautifulSoup
import os
import urllib.request
import time
import random
from random import randint


headers = {
                'Host': 'hotel.meituan.com',
                'Referer': 'https://bj.meituan.com/',
                'Origin': 'https://hotel.meituan.com',
                'Upgrade-Insecure-Requests': '1',
                'X-Forwarded-For': str(randint(1, 255))+'.'+str(randint(1, 255))+'.'+str(randint(1, 255))+'.'+str(randint(1, 255)),
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
                'Cookie': '__mta=209679917.1536661008235.1537029426912.1541775744984.3; _lxsdk_cuid=165c821b2f9c8-06b948215d2698-1033685c-1aeaa0-165c821b2f9c8; ci=1; rvct=1; iuuid=0488C59369FDB2D9028701A36E658A13CD33F576FEA9642B8B8C6DD8063EAAE5; cityname=%E5%8C%97%E4%BA%AC; _lxsdk=0488C59369FDB2D9028701A36E658A13CD33F576FEA9642B8B8C6DD8063EAAE5; uuid=3ea18b49256f4217a1f5.1541775736.1.0.0; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; hotel_city_id=1; hotel_city_info=%7B%22id%22%3A1%2C%22name%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22pinyin%22%3A%22beijing%22%7D; IJSESSIONID=2bx72dlj8u3w6lyustr2f3bp; _lxsdk_s=166f8fec3b7-259-a2-4b7%7C%7C9'
}
newfile = '微博.txt'
path1 = os.path.join('text', newfile)


url = 'https://hotel.meituan.com/beijing/'
res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.content, 'html.parser')

soup.encode('utf-8')
hotel_id = []
hotel_id_link = soup.select('.poi-title-wrapper a')
for i in hotel_id_link:
    hotel_id.append(i['href'].lstrip('http://hotel.meituan.com/').rstrip('/'))
print(hotel_id)

url1 = 'https://hotel.meituan.com/'+hotel_id[0]+'/#comment'
es = requests.get(url1, headers=headers)

soup1 = BeautifulSoup(res.content, 'html.parser')

soup1.encode('utf-8')
print(soup1)
print(soup1.select('J-tab-item'))
# for id in hotel_id:
#     for num in range(10,100,10):
#         url = 'https://ihotel.meituan.com/group/v1/poi/comment/'+int(id)+'?sortType=default&noempty=1&withpic=0&filter=all&limit=10&offset='+num+'&X-FOR-WITH=6KpfdQbK7ZYVCHzNlOa5Y%2FpolIwi3W%2BpGwjyAJSSNo8rlRZELb9ibL%2Ba0cUVdvFlzTuPJNp39MgoQPwnZ%2F6ZGd8PKzc7OZ26hbL5i6qQtegS20w3AgWbbn4W6hhudXzU17kdv7nOXXo6VaDkSlsRtw%3D%3D'


#Request URL: https://ihotel.meituan.com/hbsearch/HotelSearch?utm_medium=pc&version_name=999.9&cateId=20&attr_28=129&uuid=0488C59369FDB2D9028701A36E658A13CD33F576FEA9642B8B8C6DD8063EAAE5%401541779588654&cityId=1&offset=0&limit=20&startDay=20181109&endDay=20181109&q=&sort=defaults&X-FOR-WITH=ITk%2BPWGty0hwc66WB2F8MSt4PAPI0Y7FnT%2Bx3Rila8h7h5xHNZDb%2B3cnE26i2JM1MF6F53Nbk6bP3SjxkyRB4xfK7SCxUv9HcpFAibTqVIMDs3yNWKwJzBU2h0UWsHVNEy0TYkWCqTQvEVt%2FfGuX0g%3D%3D
#Request URL: https://ihotel.meituan.com/hbsearch/HotelSearch?utm_medium=pc&version_name=999.9&cateId=20&attr_28=129&uuid=0488C59369FDB2D9028701A36E658A13CD33F576FEA9642B8B8C6DD8063EAAE5%401541779762938&cityId=1&offset=20&limit=20&startDay=20181109&endDay=20181109&q=&sort=defaults&X-FOR-WITH=ITk%2BPWGty0hwc66WB2F8MSt4PAPI0Y7FnT%2Bx3Rila8gzc7ClQSS%2B5TL5SqhAZNFftCzINfg622b%2BgDqNBUaJs%2FaZAQv6UEXaCDg37VakiTkFeUku42FbBkqPNb0OHLr0xMQERU2IQl3L4gI3uwp02Q%3D%3D
#Request URL: https://ihotel.meituan.com/hbsearch/HotelSearch?utm_medium=pc&version_name=999.9&cateId=20&attr_28=129&uuid=0488C59369FDB2D9028701A36E658A13CD33F576FEA9642B8B8C6DD8063EAAE5%401541779852778&cityId=1&offset=0&limit=20&startDay=20181109&endDay=20181109&q=&sort=solds&X-FOR-WITH=ITk%2BPWGty0hwc66WB2F8MSt4PAPI0Y7FnT%2Bx3Rila8jZGiP8RV53%2B1EBwY%2F3FyeEq7qygXLLfs%2BenbRBOol5O%2FJd9%2FP%2BpBXw3kH3GoCr05PYmWNgrpCYKViL0KMjX%2FaTjtDzNYdQwY0f5KS0%2Fa3odQ%3D%3D
