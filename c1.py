# Napisać 2 wyrażenia generatorowe:
# 1. Filtrujące, które będzie przepuszczać dalej linie spełniające warunek:
# - niepuste po stripowaniu
# - nie rozpoczynające się od #
# 2. Numerujący linie

# ostateczne użycie:
if __name__ == '__main__':
    x = [
        'ala ma kota\n',
        '\n',
        '',
        '\t',
        '   ',
        ' # komentarz',
        'kot ma ale',
    ]

    with open('petla_for.py', 'rt', encoding='utf8') as f_in, \
            open('petla_for.py.out', 'wt', encoding='utf8') as f_out:
        g1 = (linia for linia in f_in
              if linia.strip() and not linia.strip().startswith('#'))
        g2 = (f'{i} {linia}' for i, linia in enumerate(g1))
        f_out.writelines(g2)
