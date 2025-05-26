t = int(input())

def rotate(arr):
    arrR = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arrR[i][j] = arr[n-1-j][i]
    return arrR

for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    arr1 = rotate(arr)
    arr2 = rotate(arr1)
    arr3 = rotate(arr2)

    print(f'#{tc}')

    for a,b,c in zip(arr1,arr2,arr3):
        print(f'{"".join(map(str,a))} {"".join(map(str,b))} {"".join(map(str,c))}')
