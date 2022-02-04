lst = []
num = int(input('How many numbers of elems in list1: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Sum of elements in given 1st list is :", sum(lst))

lst2 = []
num2 = int(input('How many numbers of elems in list2: '))
for m in range(num2):
    numbers = int(input('Enter number '))
    lst2.append(numbers)
print("Sum of elements in given 2nd list is :", sum(lst2))


if len(lst) == len(lst2):
    print ("Both Lists are of same length")
else:
    print("length of both lists are not same")

if sum(lst) == sum(lst2):
    print ("Both lists have same sum = ",sum(lst))
else:
    print ("both lists have diffrent sum",sum(lst) ,"and" , sum(lst2))

cmp = list(set(lst).intersection(lst2))

if cmp:
    print("Both lists are identical" , cmp)
else:
    print("both lists not Identical")