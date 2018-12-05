import sys

patient = len(sys.stdin.readline())
required = len(sys.stdin.readline())

if(patient >= required):
    print("go")
else:
    print("no")
