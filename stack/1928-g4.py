n = int(input())
arr = list(map(int,input().split()))
answer = [-1] * n
st = [0]

for i in range(1, n):
    while st and arr[i] > arr[st[-1]] :
        answer[st.pop()] = arr[i]
    st.append(i)
print(*answer)