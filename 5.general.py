def outer(args):
    return func(*args)

@outer(args)
def inner():
    return a + b


inner(2,3)