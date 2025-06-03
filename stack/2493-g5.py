n = int(input())
arr = [0]+list(map(int,input().split()))
answer = [0] * (n+1)
stack = []

for i in range(1,n+1):
    while stack:
        # stack_queue 탑보다 현재가 높다면
        if arr[i] > stack[-1][0]:
            # stack_queue 탑 제거  루프 끝나면 현재 원소 추가
            stack.pop()

        # stack_queue 탑보다 현재가 낮다면
        else:
            answer[i] = (stack[-1][1])
            break
    stack.append((arr[i],i))


for i in range(1,n+1):
    print(answer[i])