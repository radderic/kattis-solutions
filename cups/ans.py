import sys

cases = int(sys.stdin.readline())
cups = dict()

for i in range(cases):
    color = ''
    size = 0
    line = sys.stdin.readline().split()
    if(line[0].isdigit()):
        size = int(line[0])/2
        color = line[1]
    else:
        color = line[0]
        size = int(line[1])
    cups[size] = color

for i in range(cases):
    print(cups[sorted(cups)[i]])

