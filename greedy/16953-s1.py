import sys
input = sys.stdin.readline
n,m = map(int, input().split())
cnt = 0

while n!=m:

    if n > m:
        cnt = -2
        break
    elif str(m)[-1] == '1':
        m = m // 10
        cnt += 1

    elif m %2 == 0:
        m = m // 2
        cnt += 1

    else:
        cnt = -2
        break
print(cnt+1)






