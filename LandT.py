
def fun():
    
    s = input("Enter The String : ")
    x = input("Enter The char  to remove: ")

    a =""
    for ch in s:
        if(ch!=x):
            a+=ch
    print(a)

fun()