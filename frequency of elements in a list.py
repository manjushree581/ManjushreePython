numbers=[1,2,2,3,3,3,4,4,4,4]
frequency={}
for num in numbers:
    frequency[num]=frequency.get(num,0)+1
print("frequency of elements:", frequency)
