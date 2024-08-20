import json



CONFIG_PATH = "./config.json"
configs = {}

def config(*args):
    with open(CONFIG_PATH, 'r') as config_file:
        data = json.load(config_file)
        for el in args:
            if el in data.keys():
                configs[el] = data[el]
            else:
                raise Exception(el + " is missing")
    return configs


result = config("language", "locale", "id")
print(result)


