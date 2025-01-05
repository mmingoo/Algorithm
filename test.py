import sys, heapq

input = sys.stdin.readline
stack = []
rank = 0
while 1:
    rank += 1
    cnt = 0
    chr_list = list(input().rstrip())
    stack.clear()

    if chr_list[0] == "-":
        break

    else:
        for i in range(len(chr_list)):
            if chr_list[i] == "}":
                if stack:
                    stack.pop()
                else:
                    cnt+=1
                    stack.append("{")

            else:
                stack.append("{")

    if stack:
        cnt+=len(stack)//2

    print(f"{rank}. {cnt}")
