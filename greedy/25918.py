import sys

input = sys.stdin.readline
n = int(input())
str_list = input().strip()
stack = []
cnt = 0
max_depth = 0

for ch in str_list:
    if ch == '(':
        if len(stack) == 0 or stack[-1] == '(':
            stack.append(ch)
            cnt = len(stack)
            max_depth = max(cnt, max_depth)

        else:
            stack.pop()
    else:
        if len(stack) == 0 or stack[-1] == ')':
            stack.append(ch)
            cnt = len(stack)
            max_depth = max(cnt, max_depth)
        else:
            stack.pop()


if stack:
    print(-1)
else:
    print(max_depth)



## 두번째
N = int(input())
S = input()
min_day = 0
total = 0
for char in S:
    if char == '(':
        total += 1
    else:
        total -= 1
    if abs(total) > min_day:
        min_day = abs(total)
if total == 0:
    print(min_day)
else:
    print(-1)