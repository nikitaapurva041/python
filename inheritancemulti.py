class A:
    def dataA(self):
        print("Data from class A")
class B:
     def dataB(self):
         print("Data from class B")
class C(A,B):
    def dataC(self):
        print("Data from class C")
object=C()
object.dataA()
object.dataB()
object.dataC()