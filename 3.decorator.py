def deco(res):
    def inner(*args):
        print(f'{args[0]} {args[1]} is coming')
        res(*args)
    return inner

@deco
def outer(first, last):
    print(f"Welcome {first} {last}")


outer('John', 'Dou')
