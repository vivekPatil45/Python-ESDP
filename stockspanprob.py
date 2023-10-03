def fun():
    
    
    n = int(input("N = "))
    price = []
    ans =[]
    for i in range(n):
        temp = int(input())
        price.append(temp)
        if(i==0):
            ans.append(1)
        else:
            if(price[i-1]>price[i]):
                ans.append(1)
            else:
                ans.append(2)
    
    print(price)
    print(ans)

    
    


fun()