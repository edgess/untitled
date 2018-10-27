import urllib2
import re
from bs4 import BeautifulSoup
#encoding = utf-8
class Crawler:
  def main(self):
    page = urllib2.urlopen('http://192.168.10.9/CH/home/home.html', timeout=10)
    data = page.read()
    # print data
    soup = BeautifulSoup(data, "html.parser")
    print len(data)
    print soup
    # for tag in soup.find_all("td"):
    #   if len(tag.string)>15:
    #     print (tag.string)

if __name__ == '__main__':
  me=Crawler()
  me.main()