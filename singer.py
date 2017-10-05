class Foo:
    instance = None
    def __init__(self, name):
        self.name = name
    @classmethod
    def get_instance(cls):
        if cls.instance:
            return cls.instance
        else:
            obj = cls("python")
            cls.instance = obj
            return obj
obj = Foo.get_instance()
obj.name = 'eer'
print(obj)
obj1 = Foo.get_instance()
print(obj1)
print (obj1.name)
