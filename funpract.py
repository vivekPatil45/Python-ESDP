
def conversion(n):
    binary = bin(n)
    octal = oct(n)
    Hexadecimal = hex(n)
    print("Binary : ",binary," Octal : ",octal," Hexadecimal : ",Hexadecimal)
# conversion(7)

def arithOperatation(a,b):
    print(a,b)
    print("Addition : ",a+b," Subtraction : ",a-b," Multiplication : ",a*b," Division : ",a/b)
# arithOperatation(4,5)

def cube(n):
    print("Cube of ",n," = ",n**3)
# cube(3)

import time




def isPrime(n):
    if(n==0 or n==1):
        return False
    if(n==2 or n==3):
        return True
    if(n%2==0  or n%3==0):
        return False
    i=5
    while i*i<n:
        if(n%(i+2)==0 or n%(i)==0):
            return False
        i+=6
    return True
def print1to100Prime():
    ls=[]
    i=1
    while i<=100:
        if(isPrime(i)):
            ls.append(i)
        i+=1
    print(ls)

# start = time.time()
# print1to100Prime()
# end = time.time()
# print(end - start)

# factorial
def fact(n):
    if n==0 :
        return 1
    return n*fact(n-1)

# Reverse of number
def reverse(n):
    rev=0
    while n!=0:
        rev=rev*10+(n%10)
        n//=10
    return rev


# Reverse of number
def isPal(n):
    temp=n
    rev=0
    while n!=0:
        rev=rev*10+(n%10)
        n//=10
    return rev == temp



# Print Fiboanaci number upto limit
def fib(n):
    n1=0
    n2=1
    ls=[]
    ls.append(0)
    ls.append(1)
    i=2
    while i<=n:
        n3=n1+n2
        ls.append(n3)
        n1=n2
        n2=n3
        i+=1
    print(ls)
# fib(10)

def menuDrivenProg():
    while True:
        print("--------------------------")
        print("1.Arithmetic Operation")
        print("2.Factorial Number")
        print("3.Find Power ")
        print("4.Reverse Number ")
        print("5.Palindrom Number ")
        print("6.Is Prime Number ")
        print("7.Exit")
        print("--------------------------")
        ch = int(input("Enter Your Choice = "))
        print("--------------------------")
        
        if ch==1:
            a = int(input("Enter First Number = "))
            b = int(input("Enter Second Number = "))
            arithOperatation(a,b)
        elif ch==2:
            n = int(input("Enter Any Number = "))
            print("Factorial of ",n," = ",fact(n))
        elif ch==3:
            n = int(input("Enter Any Number = "))
            pow(n)
        elif ch==4:
            n = int(input("Enter Any Number = "))
            print("Revers of ",n," = ",reverse(n))
        elif ch==5:
            n = int(input("Enter Any Number = "))
            if isPal(n):
                print("Palindrom Number")
            else: 
                print("Not Palindrom Number")
        elif ch==6:
            n = int(input("Enter Any Number = "))
            if isPrime(n):
                print("Prime Number")
            else: 
                print("Not Prime Number")
        elif ch==7:
            break
        else: 
            print("Enter The valid input")

# menuDrivenProg()

def prob():
    print("---------------------")
    noOfSem = int(input("Enter No of Semester = "))
    print("---------------------")
    d = {}
    noOfSubEachSem=[]
    for i in range(noOfSem):
        temp =int(input(f"Enter The No of Subject in {i+1} = "))
        noOfSubEachSem.append(temp)
        d[i+1]=[]
    for i in range(noOfSem):
        print("Marks Obtained in Semester ",i+1,"  = ")
        for j in range(noOfSubEachSem[i]):
            temp=int(input())
            d[i+1].append(temp)
    
    print("---------------------")
    print(d)
    for i in range(noOfSem):
        print(f"Maximum mark in {i+1} semester = {max(d[i+1])}")
        
    print("---------------------")

# prob()     



# Recursion
def fact(n):
    if n==0 :
        return 1
    return n*fact(n-1)

def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return (fibo(n-1)+fibo(n-2))





print(fibo(6))