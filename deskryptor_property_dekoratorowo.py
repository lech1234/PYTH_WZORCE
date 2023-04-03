class Czlowiek:
    __slots__ = ['imie',
                 'nazwisko']

    @property
    def imie_nazwisko(self):
        w = f'{self.imie} {self.nazwisko}'
        print('Getter', w)
        return w

    @imie_nazwisko.setter
    def imie_nazwisko(self, i_naz):
        print('Setter', i_naz)
        i, n = i_naz.split()
        self.imie = i
        self.nazwisko = n

    @property
    def przedrostek(self):
        return 'Mr'

    def __init__(self, imie_nazwisko):
        self.imie_nazwisko = imie_nazwisko


c = Czlowiek('Jan Kowalski')
print(c.imie_nazwisko)
c.imie_nazwisko = 'Adam Nowak'
print(c.imie_nazwisko)
print(c.przedrostek)
c.przedrostek = 'Mrs'