import sys

word = sys.stdin.readline().strip()
word = word.lower()

per = "per"
perPos = 0
count = 0

for c in word:
    if(c != per[perPos]):
        count += 1
    perPos += 1
    if(perPos > 2):
        perPos = 0

print(count)
        
