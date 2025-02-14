import sys
input = sys.stdin.readline

k,l = map(int,input().split())
dict = {}
for i in range(l):
    num = input().strip()
    dict[num] = i


arr = sorted(dict.items(), key = lambda x :x[1])

for i in range(min(k, len(arr))):
    print(arr[i][0].strip())

