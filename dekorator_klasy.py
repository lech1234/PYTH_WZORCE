WERSJA = '1.2.3'


def dodaj_wersje(klasa):
    klasa.wersja = WERSJA
    return klasa


@dodaj_wersje
class A:
    ...


print(A.wersja)
