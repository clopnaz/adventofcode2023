RED = 'red'
GREEN = 'green'
BLUE = 'blue'
colors = [RED, GREEN, BLUE]
totals = {
  'red': 12, 
  'green': 13, 
  'blue': 14, 
} 
total = 0 
for line in open('input.txt'):
  splitline = line.partition(':')
  if ('Game' not in splitline[0]):
    print('error')
    breakpoint()
  gameno = int(splitline[0].replace('Game ', ''))
  game = splitline[2].split(';')
  def gamepossible(game):
    # if RED not in round or GREEN not in round or BLUE not in round:
    #   print('error')
    #   breakpoint()
    for round in game:
      round = round.strip()
      draws = round.split(',')
      for draw in draws:
        draw = draw.strip()
        for color in colors: 
          if color in draw: 
            number = int(draw.replace(' ' + color, ''))
            if number > totals[color]:
              return(False)
    return(True)
  def getminima(game):
    minima = {RED: 0, GREEN: 0, BLUE: 0}
    for round in game:
      round = round.strip()
      draws = round.split(',')
      for draw in draws:
        draw = draw.strip()
        for color in colors: 
          if color in draw: 
            number = int(draw.replace(' ' + color, ''))
            if number > minima[color]:
              minima[color] = number
    return(minima)
    
  gameminima = getminima(game)
  power = gameminima[RED] * gameminima[GREEN] * gameminima[BLUE]
  total += power
print(total)
  

