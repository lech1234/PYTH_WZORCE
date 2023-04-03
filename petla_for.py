# for c in 'asdasd':
#     print(c)
#
# for e in [1, 2, 3, 4, 5]:
#     print(e)
#
# with open('tmp.txt') as f:
#     for linia in f:
#         print(linia)

# Pętla for potrafi iterować po bardzo różnych strukturach danych
x = [1, 2, 3, 4, 5]
for e in x:
    print(e)

# wyciągnięcie iteratora
i = x.__iter__()

# pobieranie wartości z iteratora lub błąd StopIteration
while True:
    try:
        w = i.__next__()
    except StopIteration:
        break
    print(w)

# wyrażenie generatorowe:
x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
g1 = (i ** 2 for i in x1)
g2 = (i / 13 for i in g1)

g2 = list(g2)

for e in g2:
    print(e)

print('-------')
for e in g2:
    print(e)


