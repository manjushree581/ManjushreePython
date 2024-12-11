num=int(input("enter a number"))
sum=0
for i in range(1,num):
  if num%1==0:
   sum+=i
  if sum==num:
    print("number is perfect number")
  else:
    print("number is not a perfect number")
