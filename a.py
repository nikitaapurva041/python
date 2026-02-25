import json
l={
    'name':"Nikita",
    'age': 23
   }
p=json.dumps(l)# json.dumps() method is used to convert a Python object into a JSON string.
print(p)
print(type(p))