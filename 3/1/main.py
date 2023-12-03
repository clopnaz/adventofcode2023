import re
total = 0 
def is_symbol(character):
  if character in '0123456789.\n':
    return False
  return True 

lines = []
for line in open('input.txt'):
  lines.append(line.strip())  
for lineno,line in enumerate(lines):
  matches = re.finditer("\d+", line)
  for match in matches:
    left_border = match.span()[0]-1
    if left_border < 0:
      left_border = 0
    right_border = match.span()[1]+1
    if right_border > len(line):
      right_border = len(line)
    # smoosh together all the characters we want to check
    string_to_check = ''
    if not (lineno == 0):
      string_to_check += lines[lineno-1][left_border:right_border] + "\n"
    string_to_check += line[left_border:right_border] + "\n"
    if not (lineno == len(lines)-1): 
      string_to_check += lines[lineno+1][left_border:right_border] + "\n"
    def has_symbol(chars):
      for char in chars:
        if is_symbol(char): 
          return True
      return False
    print("\n\n" + string_to_check)
    if has_symbol(string_to_check):
      print("added!")
      total += int(match[0])
    else:
      print("not added!")
    
    
print(total)    

    


