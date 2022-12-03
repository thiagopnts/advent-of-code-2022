import sys

print(
    sum(
        map(
            lambda c: c - 96 if c >= 97 else c - 38,
            map(
                lambda g: ord((g[0] & g[1] & g[2]).pop()),
                zip(*(iter(set(line.strip()) for line in sys.stdin),) * 3),
            ),
        ),
    ),
)
