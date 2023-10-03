


def fun():
    
    s = input("Enter The String : ")
    n = len(s)
    rev = ""
    for x in range(n-1,-1,-1):
        # print(x)
        rev += s[x]
    
    if rev == s:
        print("Given String is Palindrome")
    else:
        print("Given String is Not Palindrome")


fun()