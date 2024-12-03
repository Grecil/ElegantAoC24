import sys
import re

arr = sys.stdin.read()
exp = r"mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))"
total_sum = 0
matches = re.findall(exp, arr)
state = True
for j in matches:
    if j[2] == "do()":
        state = True
    elif j[3] == "don't()":
        state = False
    elif state:
        total_sum += int(j[0]) * int(j[1])
print(total_sum)
