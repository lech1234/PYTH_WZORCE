# napisać dekorator konwertujący wartość zwracaną do str

def do_str(f):
    def f_nowa(*args, **kwargs):
        r = f(*args, **kwargs)
        r = str(r)
        return r
    return f_nowa

@do_str
def dodaj(x, y):
    return x + y


w = dodaj(2, 5)
print(type(w))
