#!/usr/bin/python
# -*- coding: UTF-8 -*-1
class Pager:
    def __init__(self, all_count):
        self.all_count = all_count

    def f1(self):
        return 123

    def f2(self, value):
        self.value=value

    def f3(self):
        print("del p.foo")

    foo = property(fget=f1, fset=f2, fdel=f3)
p = Pager(101)
p.foo = "kkk"
print p.foo
del p.foo
p.foo.__doc__

