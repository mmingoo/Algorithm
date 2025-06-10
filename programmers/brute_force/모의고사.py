# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1

    return [i + 1 for i, v in enumerate(s) if v == max(s)]


# 내가 푼 두번쨰 방식

def solution(answers):
    correct = [0] * (3)
    max_cnt = []
    correct1 = [1, 2, 3, 4, 5]
    correct2 = [2, 1, 2, 3, 2, 4, 2, 5]
    correct3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == correct1[i % 5]:
            # print(f" i : {i} /i%5 : {i%5}/answers[i] : {answers[i]} / correct1[i%5] : {correct1[i%5]} /  ")
            correct[0] += 1
        if answers[i] == correct2[i % 8]:
            correct[1] += 1
        if answers[i] == correct3[i % 10]:
            correct[2] += 1

    max_v = max(correct)

    for i in range(len(correct)):
        if correct[i] == max_v:
            max_cnt.append(i + 1)

    return max_cnt





