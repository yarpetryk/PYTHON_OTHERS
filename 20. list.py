import re

numbers = [4, 6, 7, 70, 0, 6, 0, 7, 25]
words = ['monday', 'tuesday', 'red', 'blue', 'capital', '1234-1234' ]

def list_of_numbers(input: list) -> list:
    suma = sum([el for el in input if el > 10])
    sorted_list = [el+el for el in sorted(input) if el > 0]
    odd_values = [el for el in input if not el%2]
    print(suma)
    print(sorted_list)
    print(odd_values)

def list_of_words(input: list) -> list:
    shortest_word = [(el, len(el)) for el in input]
    specific_word = [el for el in input if not len(el) % 4]
    req_exp = [el for el in input if re.findall(r'[0-9A-Z]{4}\-[0-9A-Z]{4}', el)]
    req_exp_2 = [el for el in input if re.findall(r'[1-9]{1,}', el)]

    print(shortest_word)
    print(specific_word)
    print(req_exp)
    print(req_exp_2)

list_of_numbers(numbers)
list_of_words(words)