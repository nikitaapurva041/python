#same method with different arguments
#Arguments different based on 
# number of arguments and types of arguments.
class Area:
    def findArea(self, a=None, b=None):
        if a!=None and b!=None:
            print("Area of rectangles",+int(a*b))
        elif a!= None:
            print("Area of sequare",+int(a*a))
        else:
            print("Invalid Input")
obj=Area()
obj.findArea()
obj.findArea(10,20)
obj.findArea(14)
