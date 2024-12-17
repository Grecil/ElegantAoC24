A = int(input()[12:])
B = int(input()[12:])
C = int(input()[12:])
input()
arr = [int(i) for i in input()[9:].split(",")]


# hardcoded for my input
def run(a):
    out = []
    while a:
        b = a % 8 ^ 3
        out.append(b ^ 5 ^ (a >> b) % 8)
        a //= 8
    return out


ans = [0]
for i in range(len(arr)):
    ans = [n * 8 + a for n in ans for a in range(8) if arr[-i - 1 :] == run(n * 8 + a)]
print(ans[0])
