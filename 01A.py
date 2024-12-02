import sys

arr = [list(map(int, i.split())) for i in sys.stdin.read().split("\n")]
a, b = zip(*arr)
print(sum(abs(x - y) for x, y in zip(sorted(a), sorted(b))))
