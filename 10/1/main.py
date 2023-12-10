import collections
lines = []
S = []
for lineno,line in enumerate(open('input.txt')):
# for lineno,line in enumerate(open('example4.txt')):
  line = line.strip()
  lines.append(line)
  if 'S' in line:
    S.append([lineno, line.index('S')])
assert len(S)==1
S = S[0]
def findconnections(loc):
  x = loc[0]
  y = loc[1]
  connections = []
  if not (x==0):
    # above
    if lines[x-1][y] in ['F', '7', '|']:
      connections.append([x-1, y])
  if not (y==0): 
    # left
    if lines[x][y-1] in ['F', 'L', '-']:
      connections.append([x, y-1])  
  if not (y==len(lines[x])):
    # right
    if lines[x][y+1] in ['-', '7', 'J']:
      connections.append([x, y+1])
  if not (x==len(lines)):
    # below
    if lines[x+1][y] in ['|', 'J', 'L']:
      connections.append([x+1,y])
  assert(len(connections)==2)
  return connections
def getnext(prev, curr):
  if lines[curr[0]][curr[1]] == '-':
    next1 = [curr[0], curr[1]-1]
    next2 = [curr[0], curr[1]+1]
  if lines[curr[0]][curr[1]] == '|':
    next1 = [curr[0]-1, curr[1]]
    next2 = [curr[0]+1, curr[1]]
  if lines[curr[0]][curr[1]] == 'J':
    next1 = [curr[0]-1, curr[1]]
    next2 = [curr[0], curr[1]-1]
  if lines[curr[0]][curr[1]] == 'L':
    next1 = [curr[0]-1, curr[1]]
    next2 = [curr[0], curr[1]+1]
  if lines[curr[0]][curr[1]] == 'F':
    next1 = [curr[0]+1, curr[1]]
    next2 = [curr[0], curr[1]+1]
  if lines[curr[0]][curr[1]] == '7':
    next1 = [curr[0], curr[1]-1]
    next2 = [curr[0]+1, curr[1]]
  if prev == next1:
    return next2
  if prev == next2:
    return next1
  print('oops') 
  breakpoint()

def linestopipe(lines, S, Sconns, pipescw):
  newlines = [['.' for point in line] for line in lines]
  # replace S
  newlines[S[0]][S[1]] = 'F'
  if Sconns[0][0] == S[0] == Sconns[1][0]:
    newlines[S[0], S[1]] = '|'
  if Sconns[0][1] == S[1] == Sconns[1][1]:
    newlines[S[0], S[1]] = '-'
  for pipepoint in pipescw[1:-1]:
    newlines[pipepoint[0]][pipepoint[1]] = lines[pipepoint[0]][pipepoint[1]]
  return [''.join(line) for line in newlines]

def printlines(linestoprint):
  for line in linestoprint:
    print(line)
  print()

def isinside(lines, xy):
  # https://en.wikipedia.org/wiki/Point_in_polygon
  # if my arc goes left-right...
  # At first it seemed to work if I:
  # - exclude any horiz ('-') as 'crossings' but 
  # - include ANY amount of vertical ('|', 'L', 'F', '7', and 'J')
  # In reality, I should follow after a 'L', or 'F'.
  # - ex. 1: L-J is even. equivalent to 0 crosses 
  # - ex. 2: L-7 is odd. equivalent to 1 cross.  
  # So, pay attention to "line direction"
  # - L: arc starting from north
  # - F: arc starting from south
  # - J: arc ending toward north
  # - 7: arc ending toward south
  
  inside = False
  linex = lines[xy[0]]
  for y in range(xy[1], len(linex)):
    if linex[y] == '|':
      inside = not inside
    elif linex[y] in ['L', 'F']:
      arcstart = linex[y]
    elif linex[y] == 'J':
      if arcstart == 'L':
        # L-J is even
        pass 
      elif arcstart == 'F':
        # F-J is odd
        inside = not inside
    elif linex[y] == '7':
      if arcstart == 'L':
        # L-7 is odd
        inside = not inside
      elif arcstart == 'F':
        # F-7 is even
        pass
    
      
  return inside
      
def paint(pipelines): 
  painted = [['.' for point in line] for line in pipelines]
  for x,line in enumerate(pipelines):
    for y,point in enumerate(line):
      if not pipelines[x][y] == '.':
        # print the pipesegment the way it is
        painted[x][y] = pipelines[x][y]
        continue
      elif isinside(pipelines, [x,y]):
        painted[x][y] = 'I'
      else: 
        painted[x][y] = 'O'
  painted = [''.join(line) for line in painted]
  return painted

    
    


Scons1 = findconnections(S)
# ccwlen = [['.' for x in xrange(len(lines[0]))] for x in xrange(len(lines))]
# cwlen = ccwlen.deepcopy()
ccwlen = ['S']
cwlen = ['S']
currxy = S
nextxy = Scons1[0]
pipescw = [S, Scons1[0]] # I don't actually know (or care) which way is 'clockwise'
pipesccw = [S, Scons1[1]]
while True: 
  pipescw.append(getnext(pipescw[-2], pipescw[-1]))
  if lines[pipescw[-1][0]][pipescw[-1][1]] == 'S':
    break
# while True: 
#   pipesccw.append(getnext(pipesccw[-2], pipesccw[-1]))
#   if lines[pipesccw[-1][0]][pipesccw[-1][1]] == 'S':
#     break
 
up = range(len(pipescw))
down = list(up).copy()
down.reverse()
distances = []
for i in range(len(up)):
  distance = up[i]
  if down[i] < distance:
    distance = down[i]
  distances.append(distance)
print('max distance: %s' % max(distances))

printlines(lines)
pipelines = linestopipe(lines, S, Scons1, pipescw)
printlines(pipelines)

painted = paint(pipelines)
printlines(painted)
print(collections.Counter(''.join(painted))['I'])


