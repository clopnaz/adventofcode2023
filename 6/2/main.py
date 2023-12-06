import math
# dist = t_button * t_remaining
# t_remaining = t_total - t_button
# dist = t_button * (t_total - t_button) 
# dist = t_button * t_total - t_button**2
# solve:
# t_button = .5 * (t_total +/- (t_total**2 - 4*dist)**.5

lines = open('input.txt').readlines()
times = [int(''.join([x for x in lines[0].split()[1:]]))]
dists = [int(''.join([x for x in lines[1].split()[1:]]))]

def t_button_solve(t_total, dist):
  solus = []
  solus.append(.5 * (t_total + (t_total**2 - 4*dist)**.5))
  solus.append(.5 * (t_total - (t_total**2 - 4*dist)**.5))
  return sorted(solus)
  
def does_win(t_total, dist, t_button): 
  t_remaining = t_total - t_button 
  if dist < t_button * (t_total - t_button): 
    return True
  else:
    return False

lens = []
total = 1
for i in range(len(times)):

  solus = t_button_solve(times[i], dists[i])
  if not len(solus) == 2:
    breakpoint()
  if min(solus) < 0: 
    breakpoint()
  if max(solus) > times[i]:
    breakpoint()
  print(solus)
  solus[0] = math.ceil(solus[0])
  solus[1] = int(solus[1])
  while does_win(times[i], dists[i], solus[0]-1):
    print('bottom down') 
    solus[0] -= 1
  while not does_win(times[i], dists[i], solus[0]): 
    solus[0] += 1
  while does_win(times[i], dists[i], solus[1]+1):
    solus[1] += 1
  while not does_win(times[i], dists[i], solus[1]):
    solus[1] -= 1
  winning_times = [i for i in range(solus[0], solus[1]+1)]
  breakpoint()
  lens.append(len(winning_times))
  total *= len(winning_times)
print(lens) 
print(total)

