x = int(input("enter a number : "))
a = 0
b = 1

print (" ",a,b)

for i in range(2,x+1,1):
    print (" ",a + b)
    a,b = b , a+b
