import sys
import math

for i in sys.stdin:
    inp = int(i)
    total = 0
    k = 1

    while(k <= math.sqrt(inp)):
        if(inp % k == 0):
            if(inp / k == k):
                total += k
            else:
                total += k
                total += inp/k
        k += 1

    total -= inp

    if(total == inp):
        print('{} perfect'.format(inp))
    elif(inp >= total - 2 and inp <= total + 2):
        print('{} almost perfect'.format(inp))
    else:
        print('{} not perfect'.format(inp))
