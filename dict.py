#Dictionary in Python is a collection of keys values, used to store data values like a map, which, 
# unlike other data types which hold only a single value as an element. 

# Dict = {1: 'Hi', 2: 'Hello', 3: 'Hey'}
# print(Dict)

# Creating a Dictionary
# with Integer Keys
# Dict = {1: 'Hi', 2: 'Hello', 3: 'Hey'}
# print("\nDictionary with the use of Integer Keys: ")
# print(Dict)
  
# Creating a Dictionary
# with Mixed keys
# Dict = {'Name': 'vivek', 1: [1, 2, 3, 4]}
# print("\nDictionary with the use of Mixed Keys: ")
# print(Dict)


# all dictionary methods
def dicMethod():
    dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
    # copy() method
    dict2 = dict1.copy()
    print(dict2)
    
    # clear() method
    dict1.clear()
    print(dict1)
    
    # get() method
    print(dict2.get(1))
    
    # items() method
    print(dict2.items())
    
    # keys() method
    print(dict2.keys())
    
    # pop() method
    dict2.pop(4)
    print(dict2)
    
    # popitem() method
    dict2.popitem()
    print(dict2)
    
    # update() method
    dict2.update({3: "Scala"})
    print(dict2)
    
    # values() method
    print(dict2.values())






# Count the frequency of lisst element
# from collections import defaultdict ,Counter
# ls = [10,20,10,20,30,20,10,10]
# d = defaultdict(int)
# for i in ls:
#     d[i]+=1

# print(d)
# print(Counter(ls))


# from collections import defaultdict ,Counter
# ls = [1,1012,90,3,44,32,67,78,50,45,55,16]
# d = defaultdict(list)
# for i in ls:
#     d[i//10].append(i)

# for k,v in d.items():
#     print(f"{k} : {v}")

li = [[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12],
      [13,14,15,16]]
print(li)
# di = list(list)
for i in range(4):
    if i%2 == 0:
        for j in range(4):
            print(li[j][i],end=" ")
    else:
        for j in range(3,-1,-1):
            print(li[j][i],end=" ")
    print()


        


