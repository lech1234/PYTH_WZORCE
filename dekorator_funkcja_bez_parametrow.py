import functools


def dekorator(f):
    print('Dekoruję funkcję', f)

    @functools.wraps(f)
    def f_nowa(*args, **kwargs):
        print('Dekorator przed wywołaniem funkcji oryginalnej', args, kwargs)
        r = f(*args, **kwargs)
        print('Dekorator po wywołaniu funkcji oryginalnej', args, kwargs, r)
        return r

    print('W miejsce oryginalnej funkcji zwracam', f_nowa)
    return f_nowa


print('-' * 77)
print('Dekorowanie:')


@dekorator
def f1(x, y):
    print('f1', x, y)
    return 55


print('-' * 77)
print('Użycie udekorowanej funkcji:')

# tak naprawdę dekorator podmienia obiekt oryginalnej funkcji na nowy obiekt
# f1 = dekorator(f1)

w = f1(3, 8)
print(w)
