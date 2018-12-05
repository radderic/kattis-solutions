import sys

def sums(n):
    return round((n**2 + n)/2)

def oddSum(n):
    return n**2

def evenSum(n):
    return n**2+n

casesNum = int(sys.stdin.readline())

for x in range(casesNum):
    nums = sys.stdin.readline().split()
    pos = int(nums[0])
    val = int(nums[1])
    print('{} {} {} {}'.format(pos, sums(val), oddSum(val), evenSum(val)))
