import sys

print(
    sum(
        map(
            lambda arr: 1 if arr[0].issubset(arr[1]) or arr[1].issubset(arr[0]) else 0,
            map(
                lambda arr: [
                    set(range(arr[0][0], arr[0][1] + 1)),
                    set(range(arr[1][0], arr[1][1] + 1)),
                ],
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
    ),
)
