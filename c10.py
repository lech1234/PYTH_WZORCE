# przerobić poprzednie ćwiczenie, tak, żeby typ do którego konwertujemy wartość zwracaną był parametrem
# parametrem wejściowym dekoratora.
# Jeżeli typ nie zostanie podany to nie robimy konwersji
# parametr blokuj_bledy z wartością domyślną False
# jeżeli ten parametr będzie True, to będziemy blokować błędy konwersji ValueError i TypeError
# i zwracać wartość nieskonwertowaną
def konwertuj(typ, blokuj_bledy=False):
    def dekorator_wlasciwy(f):
        def f_nowa(*args, **kwargs):
            r = f(*args, **kwargs)
            try:
                return typ(r) if typ else r
            except (ValueError, TypeError):
                if blokuj_bledy:
                    return r
                else:
                    raise

        return f_nowa

    return dekorator_wlasciwy


# kowersja do str
@konwertuj(typ=str)
def f1(x, y):
    return x + y

print(type(f1(4, 8)), f1(4, 8))


# brak kowersj
@konwertuj(None)
def f1(x, y):
    return x + y

print(type(f1(4, 8)), f1(4, 8))

# kowersja do list
@konwertuj(typ=list, blokuj_bledy=True)
def f1(x, y):
    return x + y

print(type(f1('a', 'b')), f1('a', 'b'))

# kowersja do list - blokada błędu
@konwertuj(typ=list, blokuj_bledy=True)
def f1(x, y):
    return x + y

print(type(f1(12, 22)), f1(12, 22))

# kowersja do list - blokada błędu
@konwertuj(typ=list, blokuj_bledy=False)
def f1(x, y):
    return x + y

print(type(f1(12, 22)), f1(12, 22))