# python day1-2.py < input

import sys
import heapq


total = 0
elves = []
for line in sys.stdin:
    if line != "\n":
        total += int(line.strip())
    else:
        elves.append(total)
        total = 0

print(sum(heapq.nlargest(3, elves)))
