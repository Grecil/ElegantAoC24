import sys

rules, updates = sys.stdin.read().split("\n\n")
rules = [i.split("|") for i in rules.split("\n")]
updates = [i.split(",") for i in updates.split("\n")]
ans = 0
for i in updates:
    if not any(a in i and b in i and i.index(a) > i.index(b) for a, b in rules):
        ans += int(i[len(i) // 2])
print(ans)
