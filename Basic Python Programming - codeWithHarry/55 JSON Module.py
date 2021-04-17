import json

data = '{"var1":"harry", "var2":56}'
print(data)
parsed = json.loads(data)
print(parsed)
print(type(parsed))
print(parsed['var1'])

data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}

jscomp = json.dumps(data2)
print(jscomp)
