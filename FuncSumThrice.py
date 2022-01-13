def sumThrice(a,b,c):
    sum = 0
    thrice = 0
    
    if a==b==c:
        sum = a + b + c
        thrice = sum * 3
        
        print("sum is " , sum)
        print("sums thrice is  " , thrice)
    else:
        sum = a + b + c
        print(sum)

    
a = int(input("enter a number"))
b = int(input("enter aother number"))
c = int(input("enter yet another number"))

sumThrice(a,b,c)
