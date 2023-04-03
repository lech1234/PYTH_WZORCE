# przerobić c1.py zamieniając wyrażenia generatorowe na funkcje z yield

def filtruj(g, comment_char='#'):
    for linia in g:
        if linia.strip() and not linia.strip().startswith(comment_char):
            yield linia


def numeruj(g):
    for i, linia in enumerate(g):
        yield f'{i:3} {linia}'


if __name__ == '__main__':
    with open('petla_for.py', 'rt', encoding='utf8') as f_in, \
            open('petla_for.py.out', 'wt', encoding='utf8') as f_out:
        g1 = filtruj(f_in)
        g2 = numeruj(g1)
        f_out.writelines(g2)
