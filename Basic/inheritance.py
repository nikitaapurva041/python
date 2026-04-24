#Example of multi layer inheritance
class A:
    def demovalue1(self):
        print("Demovalue1 from class A")

class B(A):
     def demovalue2(self):
        print("Demovalue2 from class B")

object=B()
object.demovalue1()
object.demovalue2()


         
