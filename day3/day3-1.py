import sys

print(
    sum(
        map(
            lambda c: c - 96 if c >= 97 else c - 38,
            [
                ord((set(first) & set(second)).pop())
                for first, second in {
                    line[: int(len(line) / 2)]: line[int(len(line) / 2) :]
                    for line in sys.stdin
                }.items()
            ],
        )
    )
)
