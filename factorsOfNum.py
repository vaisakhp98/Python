num = int(input("enter a number "))
f = 0

for i in range(1,num+1):
    f = num % i
    if(f==0):
        print(f"{i} is a factor of {num}" )
    else:
        print(f"{i} not a factor of {num}")
