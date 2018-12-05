from sys import stdin

def factorial(n):
    if(n == 1):
        return 1;
    return n * factorial(n-1)

cases = int(stdin.readline())

for x in range(cases):
    n = int(stdin.readline())
    val = str(factorial(n))
    print(val[len(val)-1])



