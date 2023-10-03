# Constructor

class myFunction():
    def __init__(self) :
        print("Cpnstructor overloading")
    
    def func(self):
        print("func code execute")

m1 =myFunction()
m1.func()


# Constructor overloading 
class Test:
    def __init__(self) :
        print("No argument method")
    def __init__(self,a) :
        print("One argument method")
    def __init__(self,a,b) :
        print("Two argument method")

t = Test()
t = Test(10)
t = Test(10,20)
t = Test(10,20,30)


# Constructor overloading with default arguments
class Test:
    def __init__(self,a=None,b=None,c=None) :
        print("Contructor with variable number of arguments ",a,b,c)


t = Test()
t = Test(10)
t = Test(10,20)
t = Test(10,20,30)

# Constructor overloading with variable number of arguments
class Test:
    def __init__(self,*n) :
        print("Contructor with variable number of arguments")


t = Test()
t = Test(10)
t = Test(10,20)
t = Test(10,20,30)

        