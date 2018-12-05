import sys

nums = sys.stdin.readline().split()
numlist = []

for n in nums:
    numlist.append(int(n))

s = sorted(numlist)

mapping = {}
mapping['A'] = s[0]
mapping['B'] = s[1]
mapping['C'] = s[2]

order = sys.stdin.readline()
print('{} {} {}'.format(mapping[order[0]], mapping[order[1]], mapping[order[2]]))
