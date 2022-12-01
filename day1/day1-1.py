# python day1-1.py < input

import sys

total = 0
highest = 0
for line in sys.stdin:
    if line != "\n":
        total += int(line.strip())
    else:
        highest = max(highest, total)
        total = 0

print(highest)
