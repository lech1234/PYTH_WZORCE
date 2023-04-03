class Samochod:
    __slots__ = ['_dlugosc']
    ilosc_kol = 4

    def __init__(self, dlugosc):
        self._dlugosc = dlugosc

s = Samochod(123)
print(s._dlugosc)
