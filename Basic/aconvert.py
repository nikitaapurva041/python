import json
l= '{"name": "Nikita","age":26,"city":"New York"}'
p=json.loads(l)# json.loads() method is used to parse a JSON string and convert it into a Python dictionary.
print(p)
print(type(p))
for a in p:
    print(a,p[a])

