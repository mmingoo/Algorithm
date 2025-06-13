def solution(brown, yellow):
    answer = []
    total_cnt = brown + yellow
    row = 3

    while row < brown:
        for c in range(3, brown):
            if row * c == total_cnt:

                if (row - 2) * (c - 2) == yellow:
                    answer.append(c)
                    answer.append(row)
                    return answer

        row += 1

    return answer