print("Hello World")
print("This is a test file.")
if 5 > 2:
 print("Five is greater than two!", end=""),print("Five is greater than two!")
print("Hello World!",end=""),print("Have a good day.")
print(3),print(358)
print(3 + 3)
print(2 * 5)
print("I am", 35, "years old.")
x = 5
y = "John"
print(x,y)
x = 4       # x is of type int
X = "Sally" # x is now of type str
print(x,X)
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3) 
print(x)
print(y)
print(z)
x = 5
y = "John"
print(type(x))
print(type(y))    
x = "John" # is the same as
X = 'John' 
print(x) 
x, y, z = "Orange", "Banana", "Cherry"
print(x,y,z)
x = y = z = "Orange"
print(x,y,z)
x = "Python "
print(type(x))
y = "is "
z = "awesome"
print(x +y+z)
x = 54
y = "Nikita"
print(x,y)
print('Hello','World')
a="Hello"
b="World"
print(a+b)

x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()
#for global variable
x = "awesome"
def myfunc():
  X = "fantastic"
  print("Python is " + X)
myfunc()
print("Python is " + x)
#for global keyword
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
#for data type conversion
x=5
y=2.5
z= "Hello"
a=complex(x)
print(type(a))
# Quotes Inside Quotes
print("My Name is 'Nikita'")
print('I am learning "Python" programming')
# Assign String to a Variable
a="Nikita"
print(a)
# Multiline Strings
a="""Lorem Ipsum is simply 
dummy text of the printing 
and typesetting industry."""
print(a)
# Strings are Arrays
a="Hello, World!" 
print(a[1],a[7])
#Looping Through a String
for x in "banana":
    print(x)
# other methods at the end of line
for x in "banana":
    print(x, end="")
# String Length
a = "Hello, World!"
print(len(a))
