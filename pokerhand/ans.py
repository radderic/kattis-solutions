import sys

hand = sys.stdin.readline().split()

count = dict()

top = 0

for card in hand:
    #print(card[0])
    if(card[0] not in count):
        count[card[0]] = 1
    else:
        count[card[0]] += 1
    if(count[card[0]] > top):
        top = count[card[0]]

print(top)
