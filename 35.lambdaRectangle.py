l = int(input("enter a length :"))
b = int(input("enter a bredth :"))
ArRect = lambda l,b : l * b
print("Area of rectangle is ", ArRect(l,b))


h = int(input("enter a height :"))
bs = int(input("enter a base :"))
ArTria = lambda h,bs : .5*h*bs
print("Area of triangle is ", ArTria(h,bs))


a = int(input("enter a number :"))
ArSqr = lambda a: a*a
print("Area of square is ", ArSqr(a))