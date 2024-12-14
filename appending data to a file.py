with open("/content/python.txt","a") as file:
  file.write("let's learn file handling in python\n")
with open("/content/python.txt","r") as file:
  print(file.read())
