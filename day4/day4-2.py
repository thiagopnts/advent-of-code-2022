import sys

print(
    sum(
        map(
            lambda arr: 1
            if set(range(arr[0][0], arr[0][1] + 1)).intersection(
                set(range(arr[1][0], arr[1][1] + 1))
            )
            else 0,
            [
                list(
                    map(
                        lambda s: list(map(int, s.split("-"))),
                        line.strip().split(","),
                    ),
                )
                for line in sys.stdin
            ],
        ),
    ),
)
