import sys

input = sys.stdin.readline
n = int(input())
info = []
total = 0
people = 0

for i in range(n):
    x, y = map(int, input().split())
    info.append([x, y])
    total += info[i][1]

info.sort()

for i in range(n):
    people += info[i][1]

    if people >= total/2:
        print(info[i][0])
        break