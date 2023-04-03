# napisać deksryptor własny
# który będzie pamiętać w liście kolejne wartości nadawane atrybutowi
# przy każdym zapisie będzie printował listę hisotycznych wartości
import collections
class HistoriaWartosci:
    __slots__ = ['_atr_name',
                 '_historia']
    def __init__(self, atr_name):
        self._atr_name = atr_name
        # self.historia = {}
        self._historia = collections.defaultdict(list)

    def __get__(self, instance, owner):
        # print('__get__', self, instance, owner)
        # jeżeli dostęp przez instancję to many instance
        if instance:
            return getattr(instance, self._atr_name)
        # a jak przez klasę to w instance jest None
        else:
            return self

    def __set__(self, instance, value):
        # if id(instance) not in self.historia:
        #     self.historia[id(instance)] = []
        self._historia[id(instance)].append(value)
        setattr(instance, self._atr_name, value)
        # print('__set__', self, instance, value)
        # print('__set__', self._historia)

    def historia(self, instance):
        return self._historia[id(instance)]

class A:
    atr1 = HistoriaWartosci('_atr1')


a1 = A()
a1.atr1 = 99
a1.atr1 = 88
a1.atr1 = 77
a1.atr1 = 66
print(a1.atr1)
print(A.atr1.historia(a1))
a2 = A()
a2.atr1 = 999
a2.atr1 = 888
a2.atr1 = 777
a2.atr1 = 666
print(A.atr1.historia(a2))
