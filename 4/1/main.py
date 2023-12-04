from icecream import ic
import re
total = 0
for cardno, line in enumerate(open('input.txt')):
  winnums = line.split('|')[0].split(':')[1]
  winnumsset = set([int(x) for x in re.findall('\d+', winnums)])
  mynums = line.split('|')[1]
  mynumsset = set([int(x) for x in re.findall('\d+', mynums)])
  matches = winnumsset.intersection(mynumsset)
  nummatches = len(matches)
  if nummatches:
    thispoints = 2**(nummatches-1)
    total += thispoints
print(total)
  
