
#내가 푼 방식
def solution(prices):
    answer = []

    for i in range(len(prices) - 1):
        cnt = 0
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                cnt += 1
                break

        answer.append(cnt)

    answer.append(0)
    return answer



# 제대로 스택을 이용한 풀이
def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):

        while stack and stack[-1][1] > prices[i]:
            past, _ = stack.pop()
            answer[past] = i - past

        # 스택에 추가
        stack.append((i, prices[i]))

    while stack:
        past, price = stack.pop()
        answer[past] = len(prices) - 1 - past

    return answer