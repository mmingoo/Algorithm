import sys
input = sys.stdin.readline
k,l = map(int,input().split())
arr = []
for _ in range(l):
    num = int(input())

    if num in arr:
        arr.remove(num)
    arr.append(num)

for i in range(min(len(arr),k)):
    print(arr[i])