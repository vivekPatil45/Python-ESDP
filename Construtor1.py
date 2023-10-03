



# count total number of objects

class Test:
    count =0
    def __init__(self) :
        Test.count = Test.count +1
    
    @classmethod
    def showCountObject(cls):
        print("The Number Of Object are created ",cls.count)

t1 =Test()
t2 = Test()
Test.showCountObject()
t3 =Test()
t4 = Test()
Test.showCountObject()





# Passing  memeber of one class to another class
# class Employee:
#     def __init__(self,no,name,sal) :
#         self.eno = no
#         self.ename = name
#         self.esal = sal

#     def showDetails(self):
#         print("Employee no       : ",self.eno)
#         print("Employee ename    : ",self.ename)
#         print("Employee salary   : ",self.esal)

# class Test:
#     def updates(Employee):
#         Employee.esal = Employee.esal+8000
#         Employee.showDetails()

# e = Employee(101,"Vivek",20000)
# e.showDetails()
# Test.updates(e)
        