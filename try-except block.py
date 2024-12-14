try:
  num=int(input("enter a number:"))
  print(10/num)
except ZeroDivisionError:
  print("you cannot divide by zero")
except ValueError:
  print("invalid input,please enter a valid number")
