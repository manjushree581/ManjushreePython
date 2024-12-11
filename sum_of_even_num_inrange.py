start=int(input("enter the start of range: "))
end=int(input("enter the end of range: "))
even_sum=0
for num in range(start,end+1):
  if num%2==0:
    even_sum+=num
    print("the sum of even numbers:", even_sum)
