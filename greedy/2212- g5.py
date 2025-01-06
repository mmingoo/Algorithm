import sys, heapq
input = sys.stdin.readline
n = int(input())
k = int(input())

if n <= 1 or k >= n:
    print(0)
else:
    sensor = list(map(int, input().split()))
    sensor.sort()
    length = []

    for i in range(1,n):
        minus = sensor[i] - sensor[i-1]
        length.append(minus)

    length.sort()

    for i in range(min(k-1, len(length))):
        length.pop()
    print(sum(length))