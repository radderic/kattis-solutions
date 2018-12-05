from sys import stdin

vals = set()

for i in stdin:
    val = int(i)
    mod = val % 42
    vals.add(mod)

print(len(vals))

