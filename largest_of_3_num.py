num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
num3=float(input("enter the third number:"))
if num1>=num2 and num1>=num3:
  print("the largest number is", num1)
elif num2>=num3:
  print("the largest number is", num2)
else: 
  print("the largest number is", num3)
