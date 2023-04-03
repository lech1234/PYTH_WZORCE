import functools


class dekorator():
    def __init__(self, f):
        print('Dekoruję funkcję', f)
        self._f = f

    def __call__(self, *args, **kwargs):
        print('Dekorator przed wywołaniem funkcji oryginalnej', args, kwargs)
        r = self._f(*args, **kwargs)
        print('Dekorator po wywołaniu funkcji oryginalnej', args, kwargs, r)
        return r

    def __get__(self, instance, owner):
        return functools.partial(self, instance)


print('-' * 77)
print('Dekorowanie:')


class A:
    @dekorator
    def m1(self, x, y):
        print('m1', x, y)
        return 55


print('-' * 77)
print('Użycie udekorowanej funkcji:')

a = A()
w = a.m1(3, 8)
print(w)
