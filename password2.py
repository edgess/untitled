#coding=utf-8
import urllib, urllib2, HTMLParser,re

class OAParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.pd = []
    def handle_data(self, data):
        self.pd.append(data)

url2 = "http://192.168.10.183:8888/it"
url3 = "http://192.168.20.6:8012/Logon.asp"
url = "http://127.0.0.1:8080/ttt"
parm = {'userid':'yujj','password':'333444'}

res = urllib2.urlopen(url2, urllib.urlencode(parm))
print res.read()
print "------"
print res.info()
print "------"
print res.info().getheader('Set-Cookie')

print "---1---"
print re.search('.*JSESSIONID=(.*);',res.info().getheader('Set-Cookie')).group(1)
print "---2---"
print re.search('.*JSESSIONID=(.*?);',res.info().getheader('Set-Cookie')).group(1)

# parse = OAParser()
# parse.feed(r.read())
# parse.close()
