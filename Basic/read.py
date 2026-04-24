import json
f=open("users.json","r")
d=f.read()
final=json.loads(d)
for a,b in final.items():
 
 print(a,b)
