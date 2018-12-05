from sys import stdin

inp1 = stdin.readline().split()
time = int(inp1[1])
inp2 = stdin.readline().split()

def counter(vals):
    total = 0
    count = 0
    for x in vals:
        val = int(x)
        total += val
        if(total > time):
            return count
        else:
            count += 1

print(counter(inp2))
