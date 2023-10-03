
# from collections import defaultdict ,Counter

s = input("Enter the String = ")

# length of string
print(len(s))

# find the frequency of character
print(s.count("aa"))


# find occurance of a char in string
d = {}
for i in s:
    d[i]=0
for i in s:
    d[i]+=1
print(d)

# reverse a string
print(sorted(s))

# count the number of white spaces
a="vu sh dks askd saa"
print("No of spaces ",a.count(' '))

# replace character in string
s.replace("a","b")
print(s)


# 
