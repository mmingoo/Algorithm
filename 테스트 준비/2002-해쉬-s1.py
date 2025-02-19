import sys
input = sys.stdin.readline
n = int(input())
location = {}
cnt = 0
after = []

for i in range(n):
    car = input().rstrip()
    location[car] = i


for i in range(n):
    car = input().rstrip()
    after.append(car)


for i in range(n-1):
    for j in range(i+1,n):
        if location[after[i]] > location[after[j]]:
            cnt += 1
            break
print(cnt)