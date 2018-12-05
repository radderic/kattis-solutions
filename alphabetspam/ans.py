import sys


inp = sys.stdin.readline().strip()

whitespace = 0;
lowercase = 0;
uppercase = 0;
symbols = 0;

for c in inp:
    val = ord(c)
    if(val == 95):
        whitespace += 1
    elif(val >= 97 and val <= 122):
        lowercase += 1
    elif(val >= 65 and val <= 90):
        uppercase += 1
    else:
        symbols += 1

total = len(inp)

ws_ratio = float(whitespace) / float(total)
lo_ratio = float(lowercase) / float(total)
up_ratio = float(uppercase) / float(total)
sy_ratio = float(symbols) / float(total)

print(ws_ratio)
print(lo_ratio)
print(up_ratio)
print(sy_ratio)


