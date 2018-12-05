import sys

for i in sys.stdin:
    input = i.split()
    num = int(input[0])
    for x in range(num):
        print(x+1, "Abracadabra")

