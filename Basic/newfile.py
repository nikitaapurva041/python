#check type  of input type
"""name=input("name : ")
age=int(input("age :"))
price=float(input("price :"))

print("My name is",name," and my age is",age,"price is ",price)

#conditional statements

light=input("light color: ")
if light=="red":
    print("Stop")
elif light=="yellow":
    print("Get Ready")
elif light=="green":
    print("GO")
else:
    print("Signal is off")"""

#marks and grade
#A=5 & G=M
#A=2 & G=F

A=int(input("A : "))
G=input("M/F: ")
if(A==1 or A==2)and(G=="M"):
    print(" fee is 100")
elif(A==3 or A==4 or G=="F"):
    print(" fee is 200")
elif(A==5 and G=="M"):
    print(" fee is 300")
else:
    print(" no fee")
