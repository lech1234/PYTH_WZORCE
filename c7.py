# Dla klasy:
class Czlowiek:
    __slots__ = ['_imie',
                 '_nazwisko']

    def _set_imie(self, i):
        i = i.strip()
        if not i:
            raise ValueError('Imię nie może być puste')
        w = i.split()
        if len(w) == 1:
            self._imie = i.capitalize()
        elif len(w) == 2:
            i, n = w
            i = i.capitalize()
            n = n.capitalize()
            self._imie = i
            self._nazwisko = n
        else:
            raise ValueError(f'Niepoprawne imie: {i}')

    def _get_imie(self):
        return self._imie

    imie = property(fset=_set_imie, fget=_get_imie)

    def _set_nazwisko(self, n):
        n = n.strip()
        if not n:
            raise ValueError('Nazwisko nie może być puste')
        w = n.split()
        if len(w) == 1:
            self._nazwisko = n.capitalize()
        elif len(w) == 2:
            i, n = w
            i = i.capitalize()
            n = n.capitalize()
            self._imie = i
            self._nazwisko = n
        else:
            raise ValueError(f'Niepoprawne nazwisko: {n}')

    def _get_nazwisko(self):
        return self._nazwisko

    nazwisko = property(fset=_set_nazwisko, fget=_get_nazwisko)

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def __repr__(self):
        return f'Czlowiek({self.imie}, {self.nazwisko})'

# dodać walidację imienia i nazwiska:
# 1. Jeżeli jest puste po stripie -> Value Error
# 2. Jeżeli jest z małej litery - zamieniamy na wielką
# 3. Jeżeli split() zwraca 2 elementy (np 'Jan Kowalski') to traktujemy to jako imie nazwisko i ustawiamy
# 4. Jeżeli split() zwraca >2 elementy to ValueError

c = Czlowiek('jan', 'nowak')
print(c)
c.nazwisko = 'Adam Adamek'
print(c)
c.imie = 'Paweł Buk'
print(c)

