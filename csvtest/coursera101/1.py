import re



x = open('regex_sum_42.txt')
numlist = []

for n in x:
   #n = n.rstrip()
   stuff = re.findall('[0-9]+', n)
   numlist = stuff + numlist
'''
sum = 0
for z in numlist:
   sum = sum + int(z)
''' 

print(numlist)