mydict = {"a": 1, "b": 2, "a": 1}
new_dict = {}
for key, value in mydict.items():
    if key not in new_dict.keys():
        new_dict.setdefault(key, value)
print(new_dict)
