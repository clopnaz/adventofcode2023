import re
numerals = '1234567890'
total = 0 

lines = []
for line in open('input.txt'):
  lines.append(line.strip())  
for lineno,line in enumerate(lines):
  matches = re.finditer("\*", line)
  for match in matches:
    adjacents = []
    # what slots should it be in?
    lookingfor = set(range(match.span()[0]-1,match.span()[0]+2))
    # check line above
    if not (lineno == 0):
      dmatches = re.finditer("\d+", lines[lineno-1])
      for dmatch in dmatches:
        dmatch_range = set(range(*dmatch.span()))
        # is the number above+adjacent to the gear?
        if not lookingfor.isdisjoint(dmatch_range):
          adjacents.append(int(dmatch[0]))
    # check same line
    dmatches = re.finditer("\d+", line)
    for dmatch in dmatches: 
      dmatch_range = set(range(*dmatch.span()))
      # is the number right/left of gear?
      if not lookingfor.isdisjoint(dmatch_range):
        adjacents.append(int(dmatch[0]))
    # check line below
    if not (lineno == len(lines)-1):
      dmatches = re.finditer("\d+", lines[lineno+1])
      for dmatch in dmatches:
        dmatch_range = set(range(*dmatch.span()))
        # is the number above+adjacent to the gear?
        if not lookingfor.isdisjoint(dmatch_range):
          adjacents.append(int(dmatch[0]))
    print(adjacents)
    if len(adjacents)==2:
      total += adjacents[0]*adjacents[1]
print(total)
