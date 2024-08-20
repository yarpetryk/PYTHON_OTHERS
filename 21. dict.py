from collections import OrderedDict
import re

data = {
    'Physics': 82,
    'Math': 65,
    'history': 75,
    'literature': 25
}

data_1 = {
    'Physics': "test",
    'Math': '1234-1234',
    'history': 'http://',
    'literature': 'powerfox:stage'
}

def min_value(input: dict) -> dict:
    for key, value in input.items():
        if value == min(input.values()):
            print(key, value)

def sorted_dict(input: dict) -> dict:
    # result = OrderedDict(sorted(input.items(), key=lambda t: t[0]))
    result = {k: v for k, v in sorted(input.items(), key=lambda item: item[1])}
    print(result)

def filter_dict(input: dict) -> dict:
    result = {}
    for key, value in input.items():
        if value > 30:
            result.update({key: value})
    print(result)

def regexp_dict(input: dict) -> dict:
    result = {}
    for key, value in input.items():
        if re.findall(r'[0-9A-Z]{1,}\-[0-9A-Z]{4}', value):
            result.fromkeys(key, value)
    print(result)

def regexp_dict_2(input: dict) -> dict:
    result = {}
    for key, value in input.items():
        if 'st' in key:
            result.update({key: value})
    print(result)


min_value(data)
sorted_dict(data)
filter_dict(data)
regexp_dict(data_1)
regexp_dict_2(data_1)