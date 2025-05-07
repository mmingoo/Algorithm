t = int(input())  # 이중 int() 제거

for tc in range(1,t+1):
    arr = list(input())
    stack = []
    result = 1
    for ch in arr:
        stack.append(ch)

    for ch in arr:
        if stack[-1] == ch:
            stack.pop()
        else:
            result = 0
            break

    print(f"#{tc} {result}")

