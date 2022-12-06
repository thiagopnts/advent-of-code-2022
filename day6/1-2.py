import sys
from collections import deque


def find_packet(data, size=4):
        payload = []
        curr_char = 0
        while curr_char < len(data):
            c = data[curr_char]
            if len(payload) == size:
                return curr_char
            if c in payload:
                pos = payload.index(c)
                payload = payload[pos+1:]
            payload.append(c)
            curr_char += 1

for line in sys.stdin:
    print("first part:", find_packet(line, 4))
    print("second part:", find_packet(line, 14))
