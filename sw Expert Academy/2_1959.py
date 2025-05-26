t = int(input())  # 이중 int() 제거

for tc in range(1,t+1):
    a,b = map(int,input().split())
    a_arr = list(map(int,input().split()))
    b_arr = list(map(int,input().split()))
    l = abs(a-b)
    sum_arr = []
    for i in range(l+1):
        sum = 0

        if a < b:
            for j in range(a):
                sum += (a_arr[j] * b_arr[j+i])
            sum_arr.append(sum)

        else:
            for j in range(b):
                sum += (a_arr[j+i] * b_arr[j])
            sum_arr.append(sum)
    print(f"#{tc} {max(sum_arr)}")
