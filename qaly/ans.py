
import sys


lines = int(sys.stdin.readline())
total = 0

for x in range(lines):
    line = sys.stdin.readline()
    nums = line.split()
    num1 = float(nums[0])
    num2 = float(nums[1])
    total += num1 * num2


print(total)


