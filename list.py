# Seprate the neg ,pos, and zero
# Input :  10 -1 -3 -4 0 0 45 42
# OutPut : [10, 45, 42] [-1, -3, -4] [0, 0]
def p1():
    ls =  list(map(int,input().split()))
    n = len(ls)
    pos = [0]*n
    neg = [0]*n
    zero = [0]*n
    p,n,z=0,0,0
    for i in ls:
        if i==0:
            zero[z] = i
            z+=1
        elif i<=0:
            neg[n]=i
            n+=1
        else:
            pos[p] = i
            p+=1
    print(pos[:p],neg[:n],zero[:z])

# p1()


# linear search
# 4 5 8 10 11 15 1 
def p2():
    ls =  list(map(int,input().split()))
    print(ls)
    n = len(ls)
    key = int(input("Enter The Element To Search = "))
    for i in range(n):
        if(ls[i]==key):
            print(key,"Find at Index ",i)

# p2()



# binary serach
def p3():
    ls =  list(map(int,input().split()))
    print(ls)
    s = 0 
    e =  len(ls)-1
    key = int(input("Enter The Element To Search = "))
    while s<=e :
        mid = (s+e)//2
        if ls[mid] == key:
            print(f"Element is present at {mid}")
            break
        elif ls[mid]< key:
            s = mid + 1
        else:
            e = mid-1
    else:
        print("Not Present")


# given list is palindrome

# ls =  list(map(int,input().split()))
# i = 0
# j=len(ls)-1
# while(i<=j):
#     if ls[i]!=ls[j]:
#         print("Not Palindrom list")
#         break
#     i+=1
#     j-=1
# else:
#     print("Not Palindrom list")


# dictionary
d = {
    "name":"ajay devgan",
    "age": 55,
    "salary":30000,
    "experienc":10
}

for key, val in d.items():
    print(key,val)


ls = [10,20,10,20,30,20,10,]


