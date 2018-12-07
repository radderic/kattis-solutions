import sys

cases = int(sys.stdin.readline())

#1 3 2 6 2 4

for c in range(cases):
    mn = sys.stdin.readline().split()
    n = int(mn[0])
    m = int(mn[1])

    vals = sys.stdin.readline().split()
    lhs = 0
    rhs = 0
    top = 0

    for i in range(n):
        val = int(vals[i])
        if(val == m):
            print('at pivot')
            if(rhs + lhs + m > top):
                top = rhs + lhs + m
                print('new top: ' + str(top))
            lhs = rhs
            rhs = 0
        elif(i == n-1):
            rhs += val
            if(rhs + lhs + m > top):
                top = rhs + lhs + m
        else:
            rhs += val
            print('adding to rhs: ' + str(val))
            print('LHS total: ' + str(lhs))
            print('RHS total: ' + str(rhs))

    print('Final: ' + str(top))
#    print(top)

