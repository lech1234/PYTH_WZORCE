import functools


def dekorator(p1, p2):
    print('Produkuję właściwy dekorator', p1, p2)

    def dekorator_wlasciwy(f):
        print('Dekoruję funkcję', f)

        @functools.wraps(f)
        def f_nowa(*args, **kwargs):
            print('Dekorator przed wywołaniem funkcji oryginalnej', args, kwargs, p1, p2)
            r = f(*args, **kwargs)
            print('Dekorator po wywołaniu funkcji oryginalnej', args, kwargs, p1, p2, r)
            return r

        print('W miejsce oryginalnej funkcji zwracam', f_nowa)
        return f_nowa

    return dekorator_wlasciwy


print('-' * 77)
print('Dekorowanie:')


# 1. Produkcja dekoratora
# d = dekorator('ala', 12)
# 2. Użycie dekoratora
# @d
@dekorator('ala', 12)
def f1(x, y):
    print('f1', x, y)
    return 55


print('-' * 77)
print('Użycie udekorowanej funkcji:')

w = f1(3, 8)
print(w)
