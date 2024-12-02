import sys

arr = [list(map(int, i.split())) for i in sys.stdin.read().split("\n")]
print(
    sum(
        (
            all(i[j] > i[j + 1] for j in range(len(i) - 1))
            or all(i[j] < i[j + 1] for j in range(len(i) - 1))
        )
        and all(0 < abs(i[j] - i[j + 1]) < 4 for j in range(len(i) - 1))
        for i in arr
    )
)
