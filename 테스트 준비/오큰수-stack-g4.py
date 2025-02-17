import sys
input = sys.stdin.readline
n = int(input())
answer = [-1] *n
arr = list(map(int, input().split()))
stack = [0]

for i in range(1,n):
    while stack and arr[i] > arr[stack[-1]]:
        answer[stack.pop()] = arr[i]

    stack.append(i)

print(answer)
for i in range(n):
    print(answer[i], end = ' ')