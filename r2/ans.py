import sys

for i in sys.stdin:
    input = i.split()
    r1 = int(input[0])
    s = int(input[1])
    r2 = s * 2 - r1
    print(r2)
