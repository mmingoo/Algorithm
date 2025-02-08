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