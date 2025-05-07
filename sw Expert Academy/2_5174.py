t = int(input())

def sub_tree(n):
    global cnt
    for i in range(2):
        if tree[i][n]:
            cnt+=1
            child = tree[i][n]  # 자식 노드를 별도 변수에 저장
            sub_tree(child)     # 자식 노드를 기준으로 재귀 호출

for tc in range(1,t+1):
    e,n = map(int,input().split())
    nums = list(map(int,input().split()))

    tree = [[0 for _ in range(e+2)] for _ in range(2)]

    for i in range(e):
        idx = nums[2*i]
        numbers = nums[2 * i + 1]

        if tree[0][idx] == 0:
            tree[0][idx] = numbers

        else:
            tree[1][idx] = numbers


    cnt = 1
    sub_tree(n)

    print(f"#{tc} {cnt}")

