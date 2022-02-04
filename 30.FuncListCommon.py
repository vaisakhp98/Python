def commonElems(list1,list2):
    
    if list(set(list1).intersection(list2)):
        print("are common")
    else:
        print("not common")



list1 = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    list1.append(ele)
print(list1)


list2 = []
m = int(input("Enter number of elements : "))
for i in range(0, m):
    elem = int(input())
    list2.append(elem)
    
print(list2)

commonElems(list1,list2)
