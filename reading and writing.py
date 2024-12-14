with open("/content/python.txt","w") as file:
  file.write("python is awesome!\n")
with open("/content/python.txt", "r") as file: 
 print(file.read())
