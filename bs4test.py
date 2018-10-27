# coding=utf-8
import urllib2, re, requests
from bs4 import BeautifulSoup


class Crawler:
    def main(self):
        imgurl = "http://cms.satrip.com/FILE/GALLERY/PRODUCTIMG/HBX00724/11.jpg.ico"
        print requests.get(imgurl).content

        url = 'http://cms.satrip.com'
        s = requests.session();

        # mobileHeaders = {
        #     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1',
        #     'Connection': 'keep-alive'
        # }

        print s.get(url).headers
        print s.cookies

        page = requests.get(url)
        print page.cookies


if __name__ == '__main__':
    me = Crawler()
    me.main()
