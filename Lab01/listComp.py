
list1 = ["laptop", "this", "mobile", "bigword"]
lowercaseVersion = [w.lower() for w in list1 if len(w) > 5]
print(lowercaseVersion)


list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list comprehension
specifiedList = [i for index , i in enumerate(list2) if index not in [0, 4, 5]] # index 0, 4, 5 will be removed
# index here is the index of the list2, enumerate(list2) will return a tuple (index, value) and we only need the index
# indec not in [0, 4, 5] will return true if the index is not in the list [0, 4, 5], 
# not in basically means not equal to any of the value in the list
# enumerate is being used because it will keep track of the index of the list
print(specifiedList)



x = 6

if(type(x) is not int):
    print("true")
else:
    print("false")

list1 = [1,2,3]
list2 = [4,5,6]

for item in list1:
    if item in list2:
        print("Overlapping")
    else:
        print("Not Overlapping")


a = 60
b = 13
c = 0

c = a & b;        # 12 = 0000 1100
print ("Line 1 - Value of c is ", c)

c = a | b;        # 61 = 0011 1101
print ("Line 2 - Value of c is ", c)

c = a ^ b;        # 49 = 0011 0001
print ("Line 3 - Value of c is ", c)

c = ~a;           # -61 = 1100 0011
print ("Line 4 - Value of c is ", c)

c = a << 2;       # 240 = 1111 0000
print ("Line 5 - Value of c is ", c)

c = a >> 2;       # 15 = 0000 1111
print ("Line 6 - Value of c is ", c)

