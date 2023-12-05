import re
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
      seednos = [int(x) for x in line.split(':')[1].split()]
      
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
  for row in table: 
    if row[1] <= x <= row[1] + row[2] - 1: 
      row
      return row[0] + x - row[1]
  return x
  
locationseeds = []
for seed in seednos: 
  soil = xfer(seed, seedsoil)
  fertilizer = xfer(soil, soilfertilizer)
  water = xfer(fertilizer, fertilizerwater)
  light = xfer(water, waterlight)
  temp = xfer(light, lighttemp)
  humidity = xfer(temp, temphumidity)
  location = xfer(humidity, humiditylocation)
  locationseeds.append([location, seed])
print(sorted(locationseeds))


