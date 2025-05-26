t = int(input())

for tc in range(1,t+1):
    arr = list(input())
    l = 1
    for i in range(1,len(arr)):
        if arr[0:i] == arr[0+i:0+2*i]:
            l = i
            break
    print(f'#{tc} {l}')