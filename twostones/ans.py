import sys

for i in sys.stdin:
    input = i.split()
    stoneNum = int(input[0])
    if(stoneNum % 2 != 0):
        print("Alice")
    else:
        print("Bob")

