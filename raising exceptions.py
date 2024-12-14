def check_age(age):
  if age<18:
    raise ValueError("age must be 18 or above")
    return True 
try:
  check_age(16)
except ValueError as e:
  print(e)
