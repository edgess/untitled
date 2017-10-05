#!/usr/bin/env python
#coding:utf-8
def run():
    while True:
        inp = input("请输入要访问的URL:")
#        mo,fn = inp.split('/')
        obj = __import__(inp)
        aaa = getattr(obj,'abc')
        aaa()

#run()
print '123'
