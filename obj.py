class AA():
    def act(self):
        print "run"

class BB():
    def act(self):
        print "fuck"

def cc(obj):
    obj.act()

man = AA()
fe =BB()
cc(man)
cc(fe)
