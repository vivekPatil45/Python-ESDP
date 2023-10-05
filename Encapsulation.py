

# class student:
#     def __init__(self,name,rollno):
#         self.name = name
#         self.rollno = rollno

#     def show(self):
#         print(f"Student Name {self.name} and his Roll No : {self.rollno} ")



from abc import ABC,abstractmethod

# class rcpit(ABC):
#     @abstractmethod
#     def student_details(self):
#         pass
#     @abstractmethod
#     def student_assignment(self):
#         pass
#     @abstractmethod
#     def student_marks(self):
#         pass

# class Comp_A(rcpit):
#     def student_details(self):
#         return "it will try to return the student details of comp a"
    
#     def student_assignment(self):
#         return "it will try to return the student details of comp a"

#     def student_marks(self):
#         return "it will try to return the student details of comp a"
    
    
# ca = Comp_A()
# print(ca.student_details)
# print(ca.student_assignment)
# print(ca.student_marks)



class Course(ABC): 
    def __init__(self,title,duration,price) :
        super().__init__()
        self.title = title
        self.duration = duration
        self.price = price
    @abstractmethod
    def enroll(self):
        pass
    @abstractmethod
    def get_details(self):
        pass

        
class ProgrammingCourse(Course):
    def __init__(self, title, duration, price,prog_l,instr):
        super().__init__(title, duration, price)
        self.prog_l = prog_l
        self.instr= instr
    
    def get_details(self):
        print("-----------------------")
        print("Title Of Course ",self.title)
        print("Duration Of Course ",self.duration)
        print("Price Of Course ",self.price)
        print("Programming language Of Course ",self.prog_l)
        print("Instructor Of Course ",self.instr)

        
class MathCourse(Course):
    def __init__(self, title, duration, price,level,instr):
        super().__init__(title, duration, price)
        self.prog_l = level
        self.instr= instr
    
    def get_details(self):
        print("-----------------------")
        print("Title Of Course ",self.title)
        print("Duration Of Course ",self.duration)
        print("Price Of Course ",self.price)
        print("Level Of Course ",self.prog_l)
        print("Instructor Of Course ",self.instr)

