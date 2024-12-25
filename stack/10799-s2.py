import sys
input = sys.stdin.readline
pip = list(input().strip())
stack = []
cnt = 0

for i in range(len(pip)):
    if pip[i] == '(':
        stack.append(i)

    # () 인 경우
    else:
        if pip[i-1] == '(':
            stack.pop()
            cnt += len(stack)

        # )) 인 경우
        else:
            stack.pop()
            cnt+=1

print(cnt)