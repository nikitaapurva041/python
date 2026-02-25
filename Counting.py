for n in range(1, 11):
    print("2*", n,"=", 2*n)

# 3 tables
for n in range(1,11):
    print("3*",n,"=",3*n)

# reverse order
for n in range(10,0,-1):
    print(n)

# count repeat number
d = [10, 20, 30, 10, 40, 50, 10, 10]

for i in set(d):
    if d.count(i) > 1:
        print(i, "is repeated", d.count(i), "times")

    