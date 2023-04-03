class A:
    atr1 = 'mama'

    def m1(self):
        print('A.m1')


def m1(self):
    print('m1 z klasy z metaklasy')


cls_dict = {
    'atr1': 'mama',
    'm1': m1
}

NoweA = type('A', (), cls_dict)
a = NoweA()
a.m1()


# prosta metaklasa dodająca np wersję:
def moja_meta(cls_name, cls_inh, cls_dict):
    cls_dict['version'] = '1.2.3'
    return type(cls_name, cls_inh, cls_dict)


class A(metaclass=moja_meta):
    ...


a = A()
print(a.version)
