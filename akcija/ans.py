
import sys

numCases = int(sys.stdin.readline())
numList = []

for x in range(numCases):
    val = int(sys.stdin.readline())
    numList.append(val)

l = sorted(numList)
total = sum(l)

pos = len(l)-3
while(pos >= 0):
    total -= l[pos]
    pos -= 3

print(total)

