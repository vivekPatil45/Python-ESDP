
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


# Q3

# class Shape:
#     def __init__(self):
#         pass
#     def area(self):
#         self.ar = 0
#     def perimeter(self):
#         self.per = 0
    
# class Circle(Shape):
#     def __init__(self,rad):
#         super().__init__()
#         self.rad = rad
    
#     def area(self):
#         super().area()
#         self.ar = 3.14 * self.rad * self.rad
#         print("Area Of Circle = ",self.ar)

#     def perimeter(self):
#         super().perimeter()
#         self.per = 2 * 3.14 * self.rad
#         print("Perimeter Of Circle = ",self.per)

    
# class Rectangle(Shape):
#     def __init__(self,l,b):
#         super().__init__()
#         self.l = l
#         self.b = b

    
#     def area(self):
#         super().area()
#         self.ar = self.l * self.b
#         print("Area Of Circle = ",self.ar)

#     def perimeter(self):
#         super().perimeter()
#         self.per = 2*self.l + 2*self.b
#         print("Perimeter Of Circle = ",self.per)


# Q4

class Product:
    def __init__(self,name,price,qty):
        self.name = name
        self.price = price
        self.qty = qty

class Book(Product):
    def __init__(self, name, price, qty,author,gener):
        super().__init__(name, price, qty)
        self.author = author
        self.gener = gener

    def display_details(self):
        print("Book Name ",self.name)
        print("Book Price ",self.name)
        print("Product Quantity ",self.qty)
        print("Author Name ",self.name)
        print("Book Genere ",self.gener)


class Electronics(Product):
    def __init__(self, name, price, qty,author,gener):
        super().__init__(name, price, qty)
        self.author = author
        self.gener = gener

    def display_details(self):
        print("Book Name ",self.name)
        print("Book Price ",self.name)
        print("Product Quantity ",self.qty)
        print("Author Name ",self.name)
        print("Book Genere ",self.gener)

