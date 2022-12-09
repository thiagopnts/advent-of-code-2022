import sys


m = [list(map(int, row.strip())) for row in sys.stdin]
result = (len(m[0]) * 2) + (len(m) * 2) - 4
for col in range(1, len(m)-1):
    for row in range(1, len(m[col])-1):
        # left from i,j
        if all(map(lambda v: v < m[col][row], m[col][:row])):
            result += 1
            continue
        # right from i,j
        if all(map(lambda v: v < m[col][row], m[col][row+1:])):
            result += 1
            continue
        visible = True
        for k in range(col):
            if m[k][row] >= m[col][row]:
                visible = False
                break
        if visible:
            result += 1
            continue

        visible = True
        for k in range(col+1, len(m)):
            if m[k][row] >= m[col][row]:
                visible = False
                break
        if visible:
            result += 1

print(result)
