# https://school.programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    row = 0
    column = 0
    for i in range(len(sizes)):
        sizes[i].sort(reverse=True)

    for i in range(len(sizes)):
        row = max(sizes[i][0], row)
        column = max(sizes[i][1], column)

    return row * column