def sumf(n):
    if(n!=0):
        print("Error")


n=int(input("Enter number:"))
sum=0
while(n!=0):
    sum = sum + (n%10)
    n = n//10
print("Sum=",sum)
    
