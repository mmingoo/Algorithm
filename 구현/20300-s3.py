
## 첫번째
n = int(input())
loss = list(map(int,input().split()))
total_loss = []

if len(loss) % 2 == 1:
    total_loss.append(max(loss))
    del loss[loss.index(max(loss))]


for _ in range(n//2):
    min_num = min(loss)
    max_num = max(loss)


    del loss[loss.index(min(loss))]
    del loss[loss.index(max(loss))]

    total_loss.append(min_num+max_num)

print(max(total_loss))

## 두번째
import sys
input = sys.stdin.readline
n = int(input())
loss = list(map(int,input().split()))

last_day = 0
loss.sort()
sum_list = []

# 홀수이면
if n % 2 == 1:
    last_day = loss.pop()


sum_list = [loss[i] + loss[-i-1]for i in range(len(loss)//2)]
sum_list.append(last_day)
print(max(sum_list))





