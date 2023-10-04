
n = int(input("N = "))
A = []

sum=0
for i in range(n-1):
    temp = int(input(f"A[{i}] = "))
    A.append(temp)
    sum += temp

tot = (n*(n+1))/2

print("------")
print(int(tot-sum))

