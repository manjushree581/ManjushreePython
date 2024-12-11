num=int(input("enter a number"))
count=0
while num!=0:
  num=num//10
  count+=1
  print("the number of digits is:", count)
