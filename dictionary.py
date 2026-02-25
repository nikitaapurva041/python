d={
    "course": "Python",
    "level": "Beginner",
    "duration": "3 months",
    "fees": "300",
}
# Using get() method to access value
a=d.get("course")
print(a)
# using keys() method to access keys
for b in d.keys():
 print(b)
 # using values() method to access values
 for c in d.values():
  print(c)
# using items() method to access key-value pairs
 for e, f in d.items():
    print(e, f)
#using del to remove a key-value pairdel 
del d["fees"]
print(d)
# using pop() to remove a key-value pair
print(d.pop("duration"))
# dict create using dict() constructor
dict1 = dict(name="John", age=25, city="New York")  
print(dict1)
# using update() method to update a dictionary
d.update({"level": "Intermediate"})
print(d)
#using inserting a new key-value pair
d["Address"]="123 Street"
print(d)
# using clear() method to remove all items from the dictionary
n=d.clear()
print(n)  # prints {}