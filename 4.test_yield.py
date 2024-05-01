from itertools import chain



def handler_list(param):
    week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    w = ['monday', 'tuesday']
    new = list(chain(week, w))
    for el in new:
        print(el)
        yield el+param

def main(handler_list):
    param = ' is coming'
    result = list(handler_list(param))
    # result = list(map(lambda x: x+param, week))
    print(result)


def tuple_in_dict():
    a = []
    for i in range(5):
        a.append((i, i+10))

    print(a)

tuple_in_dict()
