import sys
input = sys.stdin.readline()
n,m = map(int, input.split())

rs = []
chk = [False] * (n+1)

def recur(start):
    if len(rs) == m:
        print(' '.join(map(str, rs)))
        return

    for i in range(start, n+1):
        if i not in rs:
            rs.append(i)
            recur(i+1)
            rs.pop()

recur(1)


