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
