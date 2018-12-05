import sys


contestent = 1
topScore = 0
topContestent = 0

for i in sys.stdin:
    scores = i.split()
    total = 0
    for score in scores:
        score = int(score)
        total += score

    if(total > topScore):
        topScore = total
        topContestent = contestent

    contestent += 1

print("{} {}".format(topContestent, topScore))

