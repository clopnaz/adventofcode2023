from icecream import ic
import re
total = 0
cardcount = {}
lines = []
for cardno, line in enumerate(open('input.txt')):
  lines.append(line)
  cardcount[cardno] = 1
for cardno, line in enumerate(lines):
  winnums = line.split('|')[0].split(':')[1]
  winnumsset = set([int(x) for x in re.findall('\d+', winnums)])
  mynums = line.split('|')[1]
  mynumsset = set([int(x) for x in re.findall('\d+', mynums)])
  matches = winnumsset.intersection(mynumsset)
  for matchno, match in enumerate(matches): 
    ic(cardcount[cardno + matchno + 1])
    cardcount[cardno + matchno + 1] += 1*cardcount[cardno]
    ic(cardcount[cardno + matchno + 1])
    
  
for cardno, lines in enumerate(lines):
  total += cardcount[cardno]
  
print(total)
  
