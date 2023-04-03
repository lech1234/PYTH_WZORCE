class MojDeskryptor:
    def __init__(self, atr_name):
        print('konstruktor deskryptora', atr_name)
        self.atr_name = atr_name

    def __get__(self, instance, owner):
        print('__get__', self, instance, owner)
        return getattr(instance, self.atr_name)

    def __set__(self, instance, value):
        setattr(instance, self.atr_name, value)
        print('__set__', self, instance, value)

    def __delete__(self, instance):
        print('__delete__', self, instance)
        delattr(instance, self.atr_name)


class A:
    atr1 = MojDeskryptor('_atr1')


a = A()

a.atr1 = 66
print(a.atr1)
