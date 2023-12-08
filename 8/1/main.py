import collections
nodes = {}
for lineno,line in enumerate(open('input.txt')):
  line = line.strip()
  if lineno == 0:
    dirs = collections.deque([dir for dir in line])
  elif line:
    line = line.split()
    if lineno == 2:
      currnode = line[0]
    nodes[line[0]] = {'L':line[2].strip('(,'), 'R':line[3].strip(')')}

steps = 0 
while currnode != 'ZZZ':
  steps += 1
  currnode = nodes[currnode][dirs[0]]
  dirs.rotate(-1)
print(steps)  

    
