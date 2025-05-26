t = int(input())  # 이중 int() 제거

for tc in range(1,t+1):
    n = int(input())
    nums = list(map(int,input().split()))
    nums.sort()
    result = ' '.join(map(str,nums))
    print(f"#{tc} {result}")