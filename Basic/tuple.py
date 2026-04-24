t=(10,20,30,40,50,60,60)
# type of tuple
print(type(t))
# accessing tuple elements using indexing
n=t[3]
print(n)
# length of tuple
l=len(t)
print(l)
# finding index of an element
l=len(t)
for i in range(l):
 print(t[i])
 print(i)
# iterating through a tuple using for loop
for a in t:
 print(a)
# for min value in tuple
c=min(t)
print(c)
# for max value in tuple
d=max(t)
print(d)
# find the no. of count of an element in tuple
e=t.count(60)
print(e)
# no. of index of an element in tuple
f=t.index(20)
print(f)
#sum of tuples
g=sum(t)
print(g)
