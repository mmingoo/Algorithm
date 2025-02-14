n = int(input())
stack = []
arr = [int(input())for i in range(n)]
cnt = 0

for i in arr:
    while stack and stack[-1] <= i:
        stack.pop()

    cnt += len(stack)
    stack.append(i)
print(cnt)