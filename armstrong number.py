num = int(input("Enter a number: "))
order = len(str(num))
armstrong_sum = sum(int(digit)**order for digit in str(num))
if num == armstrong_sum:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
    
