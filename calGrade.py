class StudentInfo:
    def __init__(self,name,rollno,address,percentage):
        self.name=name
        self.rollno=rollno
        self.address=address
        self.percentage= percentage
        
    def showInfo(self):
        print("name = ",self.name)
        print("rollno = ",self.rollno)
        print("address = ",self.address)
        print("percentage = ",self.percentage)
        if self.percentage >=75:
            print("Grade = Distination")
        elif self.percentage >=60 :
            print("Grade = First class")
        elif self.percentage >=40 :
            print("Grade = second class")
        else:
            print("Student is Fail")
        
        
name = input("Enter name = ")
rollno = input("Enter rol no = ")
address = input("Enter address = ")
percentage = int(input("Enter percentage = "))
si = StudentInfo(name,rollno,address,percentage)
print("=========================")
si.showInfo()
print("==========================")
​
        
