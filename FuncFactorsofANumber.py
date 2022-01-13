def factors(number):
    f=0
    for i in range(1,number + 1):
        f = number % i
        if(f==0):
            print(f"{i} is a factor of {number}" )
        else:
            print(f"{i} not a factor of {number}")
            
number = int(input("enter a number "))
factors(number)
