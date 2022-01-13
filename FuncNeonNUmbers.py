def Neon(number):
    sum = 0
    square = 0

    square = number * number
    print(square, "is Square")
    
    while(number != 0):
        sum = sum + (number % 10)
        number = number // 10
        print(sum, " is sum")
        

number = int(input(" enter a number"))
Neon(number)
    
