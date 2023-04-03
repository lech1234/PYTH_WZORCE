import faker


class Pracownik:
    __slots__ = [
        'imie',
        'stawka_norm',
        'stawka_nad',
        '_zarobki'
    ]

    def __init__(self, imie, stawka_norm, stawka_nad):
        self.imie = imie
        self.stawka_norm = stawka_norm
        self.stawka_nad = stawka_nad
        self._zarobki = 0

    def pracuj(self, ile_h):
        """
        Nalicza wynagrodzenie.

        <= 8 wg stawki normalnej
        > 8 wg stawki nadgodzinowej
        naliczamy w liczniku wewnątrz instancji
        """
        if ile_h > 8:
            self._zarobki += self.stawka_norm * 8 + self.stawka_nad * (ile_h - 8)
        else:
            self._zarobki += self.stawka_norm * ile_h

    def wyplata(self):
        '''
        Zwraca zarobki i resetuje licznik
        '''
        tmp = self._zarobki
        self._zarobki = 0
        return tmp

    def __repr__(self):
        return f'{self.__class__.__name__}"({self.imie})"'


class Kierownik(Pracownik):
    __slot__ = ['bonus_kierownika']
    """
    Klasa kierownik.

    Kierownik zarabia jak pracownik, ale dodatkowo jeżeli zostanie w pracy co najmniej 10h to dostanie
    kwotową premię kierownika.
    """

    def __init__(self, imie, stawka_norm, stawka_nad, bonus_kierownika):
        super().__init__(imie, stawka_norm, stawka_nad)
        self.bonus_kierownika = bonus_kierownika

    def pracuj(self, ile_h):
        # wywołać pracuj z klasy bazowej
        super().pracuj(ile_h)
        # naliczyć bonus kierownika
        if ile_h >= 10:
            self._zarobki += self.bonus_kierownika


class Dyrektor(Kierownik):
    __slot__ = ['bonus_dyrektora']

    def __init__(self, imie, stawka_norm, stawka_nad, bonus_kierownika, bonus_dyrektora):
        super().__init__(imie, stawka_norm, stawka_nad, bonus_kierownika)
        self.bonus_dyrektora = bonus_dyrektora

    def pracuj(self, ile_h):
        # wywołać pracuj z klasy bazowej
        super().pracuj(ile_h)
        # naliczyć bonus kierownika
        self._zarobki += self.bonus_dyrektora


def zatrudnij_zespol(ilu_pracownikow, ilu_kierownikow, ilu_dyrektorow):
    """
    Zwraca listę zpracowników o podanych ilościach.
    Zarobki i bonusy - wszyscy takie same.
    * Użyć paczki faker do generacji przykładowych imion.

    :param ilu_pracownikow:
    :param ilu_kierownikow:
    :param ilu_dyrektorow:
    :return:
    """
    f = faker.Faker('PL-pl')
    lista_p = []
    lista_p += (Pracownik(f.first_name(), 20, 40) for _ in range(ilu_pracownikow))
    lista_p += (Kierownik(f.first_name(), 20, 40, 200) for _ in range(ilu_kierownikow))
    lista_p += (Dyrektor(f.first_name(), 20, 40, 200, 1000) for _ in range(ilu_dyrektorow))
    return lista_p


if __name__ == '__main__':
    lista_pracownikow = zatrudnij_zespol(10, 3, 2)
    for p in lista_pracownikow:
        p.pracuj(2)
        p.pracuj(12)
        p.pracuj(9)
    fundusz_plac = sum(p.wyplata() for p in lista_pracownikow)
    print(fundusz_plac)
