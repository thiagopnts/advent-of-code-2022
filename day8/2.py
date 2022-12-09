import sys
from functools import reduce

m = [list(map(int, row.strip())) for row in sys.stdin]
highest_score = 0
for col in range(1, len(m)-1):
    for row in range(1, len(m[col])-1):
        trees = [0,0,0,0]
        # left
        for v in reversed(m[col][:row]):
            if v < m[col][row]:
                trees[0] += 1
                continue
            if v >= m[col][row]:
                trees[0] += 1
                break
        # right
        for v in m[col][row+1:]:
            if v < m[col][row]:
                trees[1] += 1
                continue
            if v >= m[col][row]:
                trees[1] += 1
                break
        # up
        for k in reversed(range(col)):
            if m[k][row] < m[col][row]:
                trees[2] += 1
                continue
            if m[k][row] >= m[col][row]:
                trees[2] += 1
                break

        # down
        for k in range(col+1, len(m)):
            if m[k][row] < m[col][row]:
                trees[3] += 1
                continue
            if m[k][row] >= m[col][row]:
                trees[3] += 1
                break
        highest_score = max(highest_score, reduce(lambda a,b: a * b, trees))
print(highest_score)
