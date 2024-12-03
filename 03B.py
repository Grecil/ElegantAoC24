import sys
import re

arr = sys.stdin.read()
exp = r"mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))"
total_sum = 0
matches = re.findall(exp, arr)
state = True
for j in matches:
    if "do()" in j:
        state = True
    elif "don't()" in j:
        state = False
    elif state:
        total_sum += int(j[0]) * int(j[1])
print(total_sum)
