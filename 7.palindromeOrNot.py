num = int(input("enter a number : "))
ld = 0
rev = 0
temp = num

while(num != 0):
    ld = num % 10 
    rev = rev * 10 + ld
    num = num // 10
    
if(temp == rev):
    print("it is a palandrome")
else:
    print("it is not a palendrome")