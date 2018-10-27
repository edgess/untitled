# coding=utf-8
import requests, re


class Crawler:
    def main(self):
        s = requests.get('http://cms.satrip.com')
        # print s.headers.get('Set-Cookie')
        print re.search('.*ASP.NET_SessionId=(.*?);', s.headers.get('Set-Cookie')).group(1)

if __name__ == '__main__':
    me = Crawler()
    me.main()
