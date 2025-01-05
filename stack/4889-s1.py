import sys
input = sys.stdin.readline
rank = 0

while True:
    stack = []
    cnt = 0
    s = list(map(str,input().rstrip()))
    rank += 1

    if '-' in s:
        break

    for ch in s:
        if ch == "{":
            stack.append(ch)
        else:
            if stack:
                stack.pop()
            
            else:
                cnt += 1
                stack.append('{')

    cnt += len(stack)//2
    print(f"{rank}. {cnt}")




# 두번째 풀이 - 맞춤
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
