#List comprehension
n=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
m=[]
for x in n:
    if "S" in x:
        m.append(x)
print(m)

#Using list comprehension in one line
a=["Varanasi","Agra","Delhi","Mumbai","Chennai","Kolkata"]
b=[y for y in a if "a" in y]
print(b)

#Another example of list comprehension using conditional statements
c=["Apple","Banana","Grapes","Orange","Pineapple","Mango"]
d=[x for x in c if x!="Mango"]
print(d)

#range function with list comprehension

f=[x for x in range(10)]
print(f)

#sort in ascending order
g=[100,50,20,75,10]
g.sort()
print(g)

# sort in descending order
h=[20,5,50,10,70,30]
h.sort(reverse=True)
print(h)


