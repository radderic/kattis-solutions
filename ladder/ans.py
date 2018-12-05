import sys
import math

values = sys.stdin.readline().split()

hei = int(values[0])
ang = int(values[1])

hyp = hei/math.sin(math.radians(ang))
print(int(math.ceil(hyp)))
