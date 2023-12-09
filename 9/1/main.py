
total = 0
def diff(nums):
  return [nums[n+1] - nums[n] for n in range(len(nums)-1) ]
for lineno,line in enumerate(open('input.txt')):
  line = line.strip()
  nums = [[int(num) for num in line.split()]]
  while any([not num==0 for num in nums[-1]]):
    if len(nums[-1])==1:
      print('lol') 
      break
    nums.append(diff(nums[-1]))
  nums[-1].append(nums[-1][-1])
  nums.reverse()
  for listno in range(1,len(nums)):
    nums[listno].append(nums[listno][-1] + nums[listno-1][-1])
  nums.reverse()
  print(nums)
  total += nums[0][-1]
print(total)

