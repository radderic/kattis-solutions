import sys

testcases = int(sys.stdin.readline())

for i in range(testcases):
    total = 0
    average = 0

    line = sys.stdin.readline().split()
    numCases = line[0]
    line.pop(0)
    for val in line:
        total += int(val)
    average = float(total) / float(numCases)

    aboveAvg = 0
    for val in line:
        if(int(val) > average):
            aboveAvg += 1

    ratio = float(aboveAvg)/float(numCases) * 100
    print("%.3f" % ratio + "%")



