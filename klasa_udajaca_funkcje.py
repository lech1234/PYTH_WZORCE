class A:
    def __call__(self, *args, **kwargs):
        print('jestem klasa, której instancja udaje funkcje', args, kwargs)
        return 55


a = A()
r = a(4,5,6, aa=99, kk=22)
print(r)