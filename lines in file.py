with open("/content/manjushreee.txt","r") as file:
  line_count = sum(1 for line in file)
  print(f'The file contains {line_count} lines.')
