class Czlowiek:
    __slots__ = ['imie',
                 'nazwisko']

    def _set_imie_nazwisko(self, i_naz):
        print('Setter', i_naz)
        i, n = i_naz.split()
        self.imie = i
        self.nazwisko = n

    def _get_imie_nazwisko(self):
        w = f'{self.imie} {self.nazwisko}'
        print('Getter', w)
        return w

    imie_nazwisko = property(fget=_get_imie_nazwisko, fset=_set_imie_nazwisko)

    def __init__(self, imie_nazwisko):
        self.imie_nazwisko = imie_nazwisko


c = Czlowiek('Jan Kowalski')
print(c.imie_nazwisko)
c.imie_nazwisko = 'Adam Nowak'
print(c.imie_nazwisko)
