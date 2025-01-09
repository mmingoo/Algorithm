import sys

input = sys.stdin.readline

n, k = map(int, input().split())
numbers = list(input().rstrip())
stack = []

for num in numbers:
    while stack and stack[-1] < num and k>0:
        stack.pop()
        k-=1
    stack.append(num)

# 스택에 최댓값 순서대로 정렬이 됐는데도 k가 0이 아닌 경우
if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))

