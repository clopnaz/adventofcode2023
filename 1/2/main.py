import re
total = 0
# n = 0
for line in open('input.txt'):
  # n += 1 
  # print(n)
  # print(line)
  words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
  nums = [str(x) for x in range(1,10)]
  # for word, num in zip(words, nums):
  #   line = line.replace(word, num) 
  matchstr = "(?=(" + r'\d|'+'|'.join(words) + "))"
  # print(matchstr)
  digits = re.findall(matchstr, line) 
  # if n==117: breakpoint()
  for digitno in range(len(digits)):
    for word, num in zip(words, nums):
      digits[digitno] = digits[digitno].replace(word, num) 
  # print('%s digits: %s sum: %s' % (line, digits, digits[0]+digits[-1]))
  total += int(digits[0] + digits[-1])
print(total)


      
