a=int(input("enter first number:"))
b=int(input("enter second number:"))
while b!=0:
   a, b = b, a % b
print("the greatest common divisor is:", a)
