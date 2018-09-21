import requests
from bs4 import BeautifulSoup
url = 'https://news.sina.com.cn/china/'
res = requests.get(url)
# print(res.encoding)
res.encoding = 'utf-8'
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
for news in soup.select('.main-content'):
    # if len(news.select('h2')) > 0:
        print(news.text)
