try:
  file=open("","r")
except FileNotFoundError:
  print("file not found")
finally:
  print("execution complete")
