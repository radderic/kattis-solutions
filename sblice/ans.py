import sys
import math

inp = sys.stdin.readline()
nums = inp.split()
matches = int(nums[0])
width = int(nums[1])
height = int(nums[2])
diag = math.sqrt(width**2+height**2)

for i in range(matches):
    length = int(sys.stdin.readline())
    if(length <= width or length <= height or length <= diag):
        print("DA")
    else:
        print("NE")

