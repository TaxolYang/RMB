import requests
from bs4 import BeautifulSoup
url = 'https://movie.douban.com/top250'
res = requests.get(url)
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text, 'html.parser')
# for p in soup.select('.title'):
#     print(p.text)
top250 = soup.find_all('div', class_='item')
# print(top250)
top250_list = top250[0].find_all('div', class_='info')
# print((top250_list))
link = top250_list[0].find('a', )['href']
# print(link)#取href后的网址


