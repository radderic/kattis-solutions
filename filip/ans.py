from sys import stdin


nums = stdin.readline().split()
num1 = nums[0]
num2 = nums[1]

num1 = int(num1[::-1])
num2 = int(num2[::-1])

if(num1 > num2):
    print(num1)
else:
    print(num2)


