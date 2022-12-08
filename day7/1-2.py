import sys

values = []
dirs = []
for line in sys.stdin:
    parts = line.strip().split()
    if parts == ['$', 'cd', '..']:
        dirs.append(values.pop())
    elif len(parts) == 3 and parts[:2] == ['$', 'cd']:
        values.append(0)
    elif parts[0].isdigit():
        values = list(map(lambda v: v+int(parts[0]), values))
dirs += values

print(sum(filter(lambda v: v < 100000, dirs)))

print(min(filter(lambda v: v >= max(dirs) + 30000000 - 70000000, dirs)))
