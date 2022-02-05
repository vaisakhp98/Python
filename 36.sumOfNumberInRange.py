num = int(input("enter a number : "))
ranges = int(input("enter a range : "))
sum = 0
while(num <= ranges):
    sum = num + sum
    num = num + 1
print(sum)