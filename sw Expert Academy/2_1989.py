t = int(input())

for tc in range(1, t + 1):
    text = input()
    stack = []

    for ch in text:
        # 스택이 비어있지 않고 스택 맨 위 문자가 현재 문자와 같으면
        if stack and stack[-1] == ch:
            # 짝이 맞으므로 제거
            stack.pop()
        else:
            # 그렇지 않으면 스택에 추가
            stack.append(ch)

    # 스택이 비어있으면 모든 문자가 짝을 이루어 제거된 것
    result = 1 if not stack else 0

    print(f"#{tc} {result}")