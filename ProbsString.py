# Reverse a string
s="abacd"
a=""
print("Before : ",s)
for i in range(len(s)-1, -1, -1):
    a+=s[i]
print("After : ",a)

# reverse word in a string 
b="I Love India"
l= []
temp=""
for i in range(len(b)):
    print(b[i])

    if(b[i]!=" "):
        temp+=b[i]   
    else:
        s=l.append(temp)
        print(temp)
        temp=""
l.append(temp)

print(l)
l.reverse()

ans=" ".join(l)
# for i in range(len(l)-1,-1,-1):
#     ans+=(l[i]+" ")

print(ans)