#String Length
a="Nikita"
b="Apurva"
print(len(a))
print(len(b))

# Check String
a="Nikita Apurva is not working as a Technical Support Engineer"
print("Support" in a)

# print only if "operation" is present
b="Nikita is working as an operation executive in Tech Mahindra"
if("operation" in b):
    print("Yes, 'operation' is present.")
    print("Yes, in b")

# Check String Not Present
c=" I want to become a Data Scientist"
print("Data Analyst" not in c)

# print only if "Data Analyst" is not present
d="I am learning Makeup course"
if "course" not in d:
    print("Yes, 'course' is not present")

# Check String Present
a="Nikita is good girl"
if "good" in a:
    print("Yes, It is present")

# Check String Not Present
b="Apurva is not working in Zoho"
if "Select" not in b:
    print("Yes, It is not available")

# String Slicing
a="Nikita Apurva"
print(a[0:10])

# Slicing from start
d="Nikita Apurva"
print(d[:3])

# Slicing to end
e= "Amazon is a good company"
print(e[3:])

# Negative Indexing
x="Nikita Apurva"
print(x[-4:-2])

# Upper Case Conversion
A="nikita apurva"
print(A.upper())

# Lower Case Conversion
B="NIKITA APURVA"
print(B.lower())

# Remove Whitespace
z="     Nikita Apurva     "
print(z.strip())

# Replace String
p="nikita rtyu yobgegh jtdh "
print(p.replace("rtyu","qwert"))

# Split String
q="Nikita apurva is working in petpooja"
l=q.split(",")
print(l)
# other way to split the string
r="Nikita Apurva Verma"
print(r.split(","))

# String Concatenation
First =" Nikita "
Second =" Apurva"
Full = First  + Second
print( Full )

# Add a space between strings
a="Nikita"
b="Apurva"
c= a + " " + b
print(c)

# Format Strings
age=29
p= f"My Name is Nikita and My age is {age} years old"
print(p)

#format sstring with other method
price=50
txt=f"I bought a new noble book {price} rupees"
print(txt)

# modifier method of format string
s= 34
txt= f" I bought a new phone in {s:.2f}  rs. amount"
print(txt)

# Math operations inside the placeholder
country="India has population of 1.4 billion"
txt=f" count the number {country} of {20*4} state in india"
print(txt)

# Escape Characters
text=" I am learning the basics of \"The Python language\" "
print(text)

#Boolean Values
i="200"
j="50"
if i>j:
    print("Yes, i is greater than j")
else:
 print("No, i is not greater than j")
 print("False")

 #Evaluate Values and Variables
 print(bool("Hello"))
 print(bool(""))

 # check for boolean values
 x=15
 b="World"
 print(bool(x))
 print(bool(b))

 #Print "YES!" if the function returns True, otherwise print "NO!"
 def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#python operations Arithmetic operations
a=10
b=5
print(a+b)  #Addition
print(a-b)	#Subtraction
print(a*b)	#Multiplication
print(a/b)  #Division
print(a**b) #Exponentiation
print(a//b) #Floor Division
print(a%b)  #Modulus

#Python Lists
mylist = ["apple", "banana", "cherry"]
print(mylist)

#List Length
mylist = ["apple", "banana", "cherry","Mango", "Paneer"]
print(len(mylist))

#List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

#List with Mixed Data Types
List1=["Amar","Anar",10,20,30,True,False]
print(List1)

#type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#List Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Access List Items
thislist=["Apple","Banana","Cherry","Pomogranate","Orange"]
print(thislist[2])

#Negative Indexing
thislist=["Apple","Banana","Cherry","Pomogranate","Orange"]
print(thislist[-1])

#Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[3:5])

#By leaving out the start value, the range will start at the first item:
thislist= ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"] 
print(thislist[:5])

#By leaving out the end value, the range will go to the end of the list:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Negative Indexing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Check if Item Exists
n=["apple","banana","cherry","orange"]
if"apple" in n:
   print("Yes, It is present in n")

#Change Item Value
thislist=["apple", "blackberry","cherry","Anar"]
thislist[3]="Mango"
print(thislist)

#Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Change the second value by replacing it with two new values:
thislist=["apple", "banana"]
thislist[1:2]=["blackcurrant","watermelon"]
print(thislist)

# Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Insert Items
d=["apple", "banana", "cherry"]
d.insert(2,"orange")
print(d)

#Insert Items at the end of the list
c=["orange","Mango"]
c.insert(1,"Pineapple")
print(c)

#Append Items
t=["Mango", " Apple", "Banana","Grapes"]
t.append("Strawberry")
print(t)

#Insert Items
f=["Mango", " Apple", "Banana","Grapes"]
f.insert(3,"Pineapple")
print(f)

#Extend List
a=["Bikram", "Patna", "Delhi"]
b=["Mumbai", "Calcutta"," Chennai"]
a.extend(b)
print(a)

# Add Any Iterable
x=["Red","Green","Blue"]
y=("Black","White")
x.extend(y)
print(x)

#Remove Specified Item
thislist = ["apple", "banana", "cherry"]  
thislist.remove("banana")
print(thislist)

#Remove Specified Index
w=["A","B","E","C","D"]
w.pop(2)
print(w)

#Remove using del keyword
v=["P","Q","R","S","T"]
del v[1]
print(v) 

#Clear the List
m=["X","Y","Z"]
m.clear()
print(m)
"""del m
print(m)""" # The above two lines will give error because the list is deleted

# Loop Through a List
n=["Dog","Cat","Rabbit"]
for x in ["Dog","Cat","Rabbit"]:
   print(x)

#Loop Through the Index Numbers
pets=["Elephant","Donkey","Rat","Mouse"]
for i in range(len(pets)):
   print(pets[i]) 

#Using a While Loop
items = ["A", "B", "C", "D", "E"]
i = 0
while i < len(items):
    print(items[i])
    i=i+2

#List Comprehension
m = ["ape", "monkey", "dog",]
[print(x) for x in m]




