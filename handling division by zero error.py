try:
  num1=int(input("enter numerator"))
  num2=int(input("enter denominator"))
  result=num1/num2
  print("result:",result)
except ZeroDivisionError:
  print("ecannot divide by zero")
except ValueError:
  print("invalid input! enter numeric values")
