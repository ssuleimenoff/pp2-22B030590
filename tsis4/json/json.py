import json

example = '{ "name":"Ayan" , "age":18, "location":"Almaty"}'

person = json.loads(example)

print(person["name"])
