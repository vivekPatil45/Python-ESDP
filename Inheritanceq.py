
# Q1

# class Point:
#     def __init__(self):
#         self.x=0
#         self.y=0
#     def Set_Cordinate(self,x,y):
#         self.x=x
#         self.y=y
    
# class New_Point(Point):
#     def __init__(self):
#         super().__init__()
#     def draw(self):
#         print(self.x," ",self.y)

# c1 = New_Point()

# c1.Set_Cordinate(4,4)
# c1.draw()


# Q2

# class Person:
#     def __init__(self,name,age) :
#         self.name = name
#         self.age  = age
    

# class Student(Person):
#     def __init__(self,name,age,id):
#         super().__init__(name,age)
#         self.student_id = id
#     def study(self):
#         print("Student ",self.student_id, " Study")

# class Teacher(Person):
#     def __init__(self,name,age,subject):
#         super().__init__(name,age)
#         self.subject = subject
#     def teach(self):
#         print("Teacher  Teaches",self.student_id)

# s1 = Student("Vivek",21,121)
# s2 = Student("Raj",20,100)
# s3 = Student("Om",22,111)
# s1.study()
# s2.study()
# s3.study()



