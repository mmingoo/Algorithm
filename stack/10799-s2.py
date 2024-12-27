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

# 2번째 방법
import sys
input = sys.stdin.readline
str_list = input()
stack = []
cnt = 0
for i in range(len(str_list)):
    if str_list[i] == '(':
        stack.append(i)
    else:
        if str_list[i-1] == "(" and str_list[i] == ")":
            stack.pop()
            cnt += len(stack)

        else:
            if stack:
                cnt += 1
                stack.pop()
print(cnt)


## 두 번째 풀이
import sys
input = sys.stdin.readline
stack = []
ing = True
rank = 0

while ing:
    cnt = 0
    rank += 1
    stack = []
    str_list = input().rstrip()

    for i in str_list:
        if i == "}":
            if stack:
                stack.pop()
            else:
                stack.append("{")
                cnt+=1

        elif i == "{":
            stack.append("{")

        elif i == "-":
            ing = False
            break

    if ing:
        cnt += len(stack) // 2
        print(f"{rank}. {cnt}")

