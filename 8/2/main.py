import collections
nodes = {}
firstnodes = []
# for lineno,line in enumerate(open('example.txt')):
for lineno,line in enumerate(open('input.txt')):
  line = line.strip()
  if lineno == 0:
    dirs = collections.deque([dir for dir in line])
  elif line:
    line = line.split()
    if line[0][-1] == 'A':
      firstnodes.append(line[0])
    nodes[line[0]] = {'L':line[2].strip('(,'), 'R':line[3].strip(')')}

currnodes = firstnodes.copy()
steps = 0 
# while True:
#   for dir in dirs: 
#     steps += 1
#     currnodes = [nodes[currnode][dirs[0]] for currnode in currnodes]
#     if currnodes[0][-1] == 'Z':
#       echo('hi') 
#       break
#   if currnodes[0][-1] == 'Z':
#     break
# print(steps)
# while not sum([node[-1] == 'Z' for node in currnodes])>2:
steps = [0 for startno in range(len(firstnodes))]
for currnodeno,currnode in enumerate(firstnodes):
  while currnode[-1] != 'Z':
    steps[currnodeno] += 1
    currnode = nodes[currnode][dirs[0]]
    dirs.rotate(-1)

print(steps)  
import math
print(math.lcm(*steps))
