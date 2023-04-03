from pprint import pprint

x = ['ala', 'Ola', 'tomek', '']

y = []
for imie in x:
    if imie:
        y.append(imie.capitalize())
print(y)

y = [imie.capitalize()
     for imie in x
     if imie]

x = ['Ford Fiesta', 'seat', 'Fiat Panda', 'Porsche 911', '', '\n', 'Aro']

# z listy x zbudować listę y - marek samochodów z listy x, zaczynających się z wielkiej litery
['Ford', 'Seat', 'Fiat', 'Porsche', 'Aro']
y = []
for s in x:
    if s.strip():
        y.append(s.split()[0].capitalize())
print(y)
y = [s.split()[0].capitalize() for s in x if s.strip()]
print(y)

# Czy wszystkie samochody to Fiat:
print(all(s.split()[0].capitalize() == 'Fiat' for s in x if s.strip()))
# Czy którykolwiek samochód to Fiat:
print(any(s.split()[0].capitalize() == 'Fiat' for s in x if s.strip()))

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = []
for r in x:
    for e in r:
        y.append(e)
y = [e for r in x for e in r]
print(y)

y = [[f'{x*y:2}' for x in range(1, 10)] for y in range(1, 10)]
pprint(y)

# słowniki
x = ['Ala', 'Ola', 'Paweł']
d = {imie: imie[-1] for imie in x}
print(d)

# zbiory
# zbiór ostatnich liter imion z x:
s = {imie[-1] for imie in x}
print(s)
