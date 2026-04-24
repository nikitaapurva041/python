class Egg:# Parent class
    def  displayinfo(self):
            print(" I like the egg curry")
class Ws(Egg):# Child class
       def  displayinfo(self):
             # here we are calling the parent class method
             # using super() function
             # same method name
             super().displayinfo()
             print(" I am happy")
obj=Ws()
obj.displayinfo()



             
