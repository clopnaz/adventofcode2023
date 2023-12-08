from icecream import ic
import collections

cardorder = 'AKQJT98765432'
transorder = '0123456789ABC'[::-1]
trans = str.maketrans(cardorder, transorder)
arctrans = str.maketrans(transorder, cardorder)
hands = []
def highcard(cardlist):
  for card in cards:
    if card in cardlist: 
      return card
for lineno,line in enumerate(open('input.txt')): 
  line = line.strip() 
  hand = line.split()[0]
  bet = line.split()[1]
  handcnt1 = collections.Counter(line.split()[0])
  handcnt2 = collections.
  twokind = 0
  threekind = 0
  fourkind = 0
  fivekind = 0 
  
  
  # 7: five of a kind
  # 6: four of a kind
  # 5: full house 
  # 4: three of a kind
  # 3: two pair
  # 2: one pair
  # 1: high card
  def rank_hand(counts):
    if counts[0][1] == 1:
      return 1
    if counts[0][1] == 2:
      if counts[1][1] == 1: 
        return 2
      return 3
    if counts[0][1] == 3: 
      if counts[1][1] == 2:
       return 5
      return 4
    if counts[0][1] == 4: 
      return 6
    if counts[0][1] == 5: 
      return 7
  rank = rank_hand(handcnt.most_common())
  hand = hand.translate(trans)
  hands.append(str(rank) + ' ' + hand + ' ' + bet)
sortedhands = []
total = 0
for handno,hand in enumerate(sorted(hands)):
  hand = hand.split()
  hand.insert(0, str(handno+1))
  hand[2] = hand[2].translate(arctrans)
  total += (handno+1) * int(hand[3])
  hand = ' '.join(hand)
  sortedhands.append(hand)
print(total)  
