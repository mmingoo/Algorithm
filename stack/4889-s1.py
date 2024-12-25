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


