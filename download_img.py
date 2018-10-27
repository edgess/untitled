# coding=utf-8
import re, requests
from bs4 import BeautifulSoup


class Crawler:
    def main(self):
        url = 'http://www.satrip.com'
        path = '/Users/edge/Desktop/pic/'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        for tag in soup.find_all("img"):
            aa = (tag.get("src"))
            if re.findall('.', aa)[0] == "/":
                aa = url + aa
            bb = path + re.search('^.*\/(.*?)$', tag.get("src")).group(1)
            print aa + " --> " + bb

            r = requests.get(aa)
            with open(bb, 'wb') as f:
                f.write(r.content)


if __name__ == '__main__':
    me = Crawler()
    me.main()
