from sys import stdin

def findDups(line):
    words = {}
    for word in line:
        if(word in words):
            print('no')
            return
        else:
            words[word] = 1
    print('yes')

line = stdin.readline().split()
findDups(line)
