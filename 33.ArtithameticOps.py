def ArithameticOps(a,b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b

    print("adding",a,"and" , b , "=",add)
    print("subtracting",a,"and" , b , "=",sub)
    print("divide",a,"and" , b ,"=",div)
    print("multiply",a,"and" , b ,"=",mul)
    

a = int(input("enter first value"))
b = int(input("enter second value"))

ArithameticOps(a,b)