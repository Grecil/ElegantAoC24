import sys

arr = [i.split() for i in sys.stdin.read().split("\n")]
for i in range(10000):
    grid = [[" "] * 103 for _ in range(101)]
    for p, v in arr:
        px, py = map(int, p[2:].split(","))
        vx, vy = map(int, v[2:].split(","))
        x, y = (px + i * vx) % 101, (py + i * vy) % 103
        grid[x][y] = "#"
    if any("#################################" in "".join(row) for row in grid):
        print(i)
        break
