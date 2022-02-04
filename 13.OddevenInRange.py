lower = int(input("enter lower limit"))
upper = int(input("enter upper limit"))

print("Even numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(1, num):
           if (num % 2) == 0:
               print(num)
               break