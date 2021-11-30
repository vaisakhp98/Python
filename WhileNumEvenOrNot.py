num = int(input("enter a number : "))
ranges = int(input("enter a range : "))

while(num <= ranges):
    if(num % 2 == 0):
        print(num)
        num = num + 1
    else:
        num = num + 1