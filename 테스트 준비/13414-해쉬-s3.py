import sys
input = sys.stdin.readline
k , l = map(int,input().split())

dict = {}

for i in range(l):
    subject = input().strip()
    dict[subject] = i

arr = sorted(dict.items(), key = lambda x:x[1])
for i in range(min(len(arr),k)):
    print(arr[i][0])

