import sys
n = int(sys.stdin.readline())
firstCar = {}
out = []
cnt = 0

for i in range(n):
    firstCar[str(sys.stdin.readline().rstrip("\n"))] = i

for _ in range(n):
    out.append(str(sys.stdin.readline().rstrip("\n")))

for j in range(n - 1):
    for k in range(j + 1, n):
        # 제일 먼저 나간 차의 들어간 순번 > 그 다음으로 나간 차의 들어간 순번
        if firstCar[out[j]] > firstCar[out[k]]:
            cnt += 1
            break
print(cnt)