#  Creating a Thread without using any class

# from threading import *

# def show():
#     for i in range(1,11):
#         print("Child Thread")

# t = Thread(target=show)   #creating a thread object
# t.start()
# for i in range(1,11):
#     print("Main Thread")


# #  Creating a Thread by extending Thread class

# from threading import *

# print(current_thread().getName())
# print(current_thread().setName("RAJ"))
# print(current_thread().getName())


# Creating a Thread without extending Thread class
from threading import *
class MyThread:
    def run(self):
        for i in range(1,11):
            print("Child Thread")

m = MyThread()
t = Thread(target=m.run)
t.join()
for x in range(1,11):
    print("Main Thread")



