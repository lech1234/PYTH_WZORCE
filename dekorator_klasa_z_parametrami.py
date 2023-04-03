import functools


class dekorator():
    """
    Dokumentacja dekoratora

    UWAGA: Wywoływać zawsze z nawiasami
    """

    def __init__(self, p1, p2):
        self._p1 = p1
        self._p2 = p2

    def __call__(self, f):
        print('Dekoruję funkcję', f)

        @functools.wraps(f)
        def f_nowa(*args, **kwargs):
            print('Dekorator przed wywołaniem funkcji oryginalnej', args, kwargs, self._p1, self._p2)
            r = f(*args, **kwargs)
            print('Dekorator po wywołaniu funkcji oryginalnej', args, kwargs, self._p1, self._p2, r)
            return r

        print('W miejsce oryginalnej funkcji zwracam', f_nowa)
        return f_nowa


print('-' * 77)
print('Dekorowanie:')


# 1. Produkcja dekoratora
# d = dekorator('ala', 12)
# 2. Użycie dekoratora
# @d
class A:
    @dekorator(11, 22)
    def m1(self, x, y):
        print('f1', x, y)
        return 55


print('-' * 77)
print('Użycie udekorowanej funkcji:')
a = A()
w = a.m1(3, 8)
print(w)
