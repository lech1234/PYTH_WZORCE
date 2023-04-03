# Uwaga - jeżeli chcę żeby instancje klasy A mogły być kluczami słowników i elementami zbiorów,
# to muszę zaimplementować haszowanie
# UWAGA - trzeba zaimplementować obie metody __eq__ i __hash__

class A:
    __slots__ = ['atr1',
                 'atr2']

    def __init__(self, a1, a2):
        self.atr1 = a1
        self.atr2 = a2

    def __repr__(self):
        return f'A(id={id(self)}, atr1={self.atr1}, atr2={self.atr2})'

    def __eq__(self, other):
        return self.atr1 == other.atr1 and self.atr2 == other.atr2

    def __hash__(self):
        return hash((self.atr1, self.atr2))


a1 = A('mama', 12)
a2 = A('mama', 12)

s = set()
s.add(a1)
s.add(a2)
print(s)
