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




