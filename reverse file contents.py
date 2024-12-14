with open('/content/python.txt', 'r') as file:
    content = file.read()
reversed_content = content[::-1]
with open('your_file.txt', 'w') as file:
    file.write(reversed_content)
