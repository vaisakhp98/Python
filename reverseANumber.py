num = int(input("enter a number : "))
rev = 0
while(num != 0):
    rev = num % 10 
    num = num // 10
    print(rev)