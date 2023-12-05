import re
import itertools
seedsoil = []
soilfertilizer = []
fertilizerwater = []
waterlight = []
lighttemp = []
temphumidity = []
humiditylocation = []

for lineno, line in enumerate(open('input.txt')):
  line = line.strip()
  if len(line) == 0: 
    continue
  if ':' in line:
    if lineno == 0:
      line0 = line
      continue
    latest = line
    print(line)
    continue
  if 'seed-to-soil' in latest: 
    seedsoil.append([int(x) for x in line.split()])
  if 'soil-to-fertilizer' in latest: 
    soilfertilizer.append([int(x) for x in line.split()])
  if 'fertilizer-to-water' in latest: 
    fertilizerwater.append([int(x) for x in line.split()])
  if 'water-to-light' in latest: 
    waterlight.append([int(x) for x in line.split()])
  if 'light-to-temperature' in latest: 
    lighttemp.append([int(x) for x in line.split()])
  if 'temperature-to-humidity' in latest: 
    temphumidity.append([int(x) for x in line.split()])
  if 'humidity-to-location' in latest: 
    humiditylocation.append([int(x) for x in line.split()])

seeds = {}
def xfer(x, table):
  least_range = None
  for row in table: 
    if row[1] <= x <= row[1] + row[2] - 1: 
      return row[0] + x - row[1], row[1] + row[2] - x
    else:
      if (row[1] - x >=0) and ((least_range == None) or (row[1] - x < least_range)):
        least_range = row[1] - x
  return x, least_range
  
locationseeds = []
def seedfun(seedno): 
  next_ranges = []
  soil,next_range = xfer(seedno, seedsoil)
  next_ranges.append(next_range)
  fertilizer,next_range = xfer(soil, soilfertilizer)
  next_ranges.append(next_range)
  water,next_range = xfer(fertilizer, fertilizerwater)
  next_ranges.append(next_range)
  light,next_range = xfer(water, waterlight)
  next_ranges.append(next_range)
  temp,next_range = xfer(light, lighttemp)
  next_ranges.append(next_range)
  humidity,next_range = xfer(temp, temphumidity)
  next_ranges.append(next_range)
  location,next_range = xfer(humidity, humiditylocation)
  next_ranges.append(next_range)
  return location,min(next_ranges)
seedtable = [int(x) for x in line0.split(':')[1].split()]
least = {'location':float('Inf')}
for i in range(0, len(seedtable), 2):
  candidate_least = {'location':float('Inf')}
  start = seedtable[i] 
  seedrangeleft = seedtable[i+1]
  while True:
    print('start: %s' % start)
    candidate_least['location'],next_range = seedfun(start) 
    candidate_least['seed'] = start
    if candidate_least['location'] < least['location']:
      least['location'] = candidate_least['location']
      least['seed'] = candidate_least['seed']
    if seedrangeleft > next_range:
      seedrangeleft -= next_range
      start += next_range
    else:   
      break
# for seed in seednos: 
# # print(sorted(locationseeds))
# 
# 
print(least)
