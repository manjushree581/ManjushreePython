word_to_search = 'python'
with open('/content/python.txt', 'r') as file:
    for line_num, line in enumerate(file, start=1):
        if word_to_search in line:
            print(f'Word found on line {line_num}: {line.strip()}')
