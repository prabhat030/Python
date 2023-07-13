class A:
    def __init__(self,a,b,c):
        self.__a=a
        self._b=b
        self.c=c
       
    def display(self):
        print("Displaying Values in class A")
        print("Value of a:",self.__a)
        print("Value of b:",self._b)
        print("Value of c:",self.c)

class B(A):
    def display(self):
        print("Displaying Values in class B")
        try:
            print("Value of a:",self.__a)
        except Exception as e:
            print("Exception Handled: ",e)
            print("Value of a can't be accessed")
        print("Value of b:",self._b)
        print("Value of c:",self.c)
        super().display()

b=B(2,3,4)
b.display()

