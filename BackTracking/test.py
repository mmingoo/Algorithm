import sys
input = sys.stdin.readline()
n,m = map(int, input.split())

rs = []
chk = [False] * (n+1)

def recur(num):
    if num == m:
        print(' '.join(map(str,rs)))
        return

    for i in range(1, n+1):
        if chk[i] == False:
            rs.append(i)
            chk[i] = True
            rs.pop()
            recur(num+1)
recur(0)