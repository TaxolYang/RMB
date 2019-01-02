from bs4 import BeautifulSoup
import requests
def main():
    headers ={
        'Host': 'www.meituan.com',
        'Referer': 'http://www.meituan.com/meishi/6570878/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate'


    }
    url ='http://hotels.ctrip.com/Domestic/tool/AjaxHotelCommentList.aspx?MasterHotelID=429527&hotel=429527&NewOpenCount=0&AutoExpiredCount=0&RecordCount=9944&OpenDate=2007-01-01&card=-1&property=-1&userType=-1&productcode=&keyword=&roomName=&orderBy=2&currentPage=3&viewVersion=c&contyped=0&eleven=4b11d533f708063545e94bf86e97ebc513f9005d2b5d1c3a5142b96c8cf02b5a&callback=CASOdZqImeTFFHIlj&_=1538198594163'
    res = requests.get(url, headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup.text)


if __name__ == '__main__':
    main()
