import sys
input = sys.stdin.readline
n = int(input())
stack = []



for _ in range(n):
    array = list(input().strip())
    for i in array:

        if i == "(":
            stack.append(i)

        elif i == ")":
            # 스택 가장 위에 #(가 있다면 ( 제거
            if stack and stack[-1] == "(":
                stack.pop()

            # 그렇지 않다면 ) 추가
            else:
                stack.append(i)

    # 스택이 다 비워졌다면
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')

    # 스택 초기화
    stack.clear()
