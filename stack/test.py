import sys
input = sys.stdin.readline
n = int(input())
stack = []

for _ in range(n):
    flag = False
    stack = []
    str_list = list(input().rstrip())

    for char in str_list:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                flag = True

    if stack or flag == True:
       print("NO")
    else:
        print("YES")
