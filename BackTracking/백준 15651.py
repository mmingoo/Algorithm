import sys

def recur(start):
    if len(rs) == m:
        print(' '.join(map(str, rs)))
        return

    for i in range(1, n+1):
            rs.append(i)
            recur(i)
            rs.pop()

input = sys.stdin.readline()
n,m = map(int, input.split())
rs = []

recur(1)


