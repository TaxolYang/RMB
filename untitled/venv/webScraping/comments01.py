import requests
from bs4 import BeautifulSoup
url = 'https://movie.douban.com/subject/1292052/comments?start=0&limit=20&sort=new_score&status=P'
res = requests.get(url)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

comment_list = soup.find_all('div', class_='comment-item')
# print(comment_list[1])
# # print(soup)
eachcomment_list = []
for item in comment_list:
    # if item.find_all('p')[0].string is not None:
        eachcomment_list.append(item.find_all('span',class_='short')[0].string)
print(eachcomment_list)
