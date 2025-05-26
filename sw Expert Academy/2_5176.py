def make_tree(n):
    global cnt

    if n <= N:
        make_tree(n * 2)

        tree[n] = cnt
        cnt += 1

        make_tree(n * 2 + 1)


t = int(input())  # 이중 int() 제거

for tc in range(1, t + 1):
    N = int(input())
    tree = [0 for i in range(N + 1)]
    cnt = 1
    make_tree(1)

    print(f"#{tc} {tree[1]} {tree[N // 2]}")

