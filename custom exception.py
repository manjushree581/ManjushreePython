class NegativeNumberError(Exception):
  pass
def check_positive(number):
  if number<0:
    raise NegativeNumberError("negative number entered")

try:
  num=int(input("enter a positive number:"))
  check_positive(num)
except NegativeNumberError as e:
  print(e)
