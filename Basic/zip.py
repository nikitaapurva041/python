l=[10,20,30,40]
l2=[1,2,3,4,5] # here 5 will be ignored if you are using zip
t=len(l)
for a,b in zip(l,l2):
    print(a,b)
# using logic to handle different length of lists
for i in range(t):
    print(l[i],l2[i])
