import sys
from collections import deque


input = [line for line in sys.stdin]
mid_point = input.index("\n")
stacks_data, moves = input[:mid_point], input[mid_point + 1 :]
stacks = {}
for id in stacks_data.pop().strip().split():
    stacks[id] = deque()

j = 0
k = 3
curr_stack = 1
while k < len(max(stacks_data)):
    for i in range(len(stacks_data)):
        item = stacks_data[i][j:k]
        if item.strip() != "":
            stacks[str(curr_stack)].append(item)
    curr_stack += 1
    j = k + 1
    k += 4

for move in moves:
    command = move.strip().split()
    qnt, orig, dest = int(command[1]), command[3], command[5]
    while qnt > 0:
        item = stacks[orig].popleft()
        stacks[dest].appendleft(item)
        qnt -= 1

print("".join(stacks[k].popleft() for k in stacks.keys()))
