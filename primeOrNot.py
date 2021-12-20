num = int(input("enter a number"))
f = 0
count = 0
for i in range(1,num+1):
    f = num % i
    if(f == 0):
        print(f"{i} is a factor of {num}")
        count += 1
    else:
        print(f" {i} is not a factor of {num}")
        
print(count)
if (count > 2):
    print("its is not a prime number")
else:
    print("it is a prime number")



    


