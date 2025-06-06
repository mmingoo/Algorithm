def solution(operations):
    answer = []
    q = []
    for ch in operations:
        if ch == "D -1" and q:
            min_idx = q.index(min(q))
            del q[min_idx]

        elif ch == "D 1" and q:
            max_idx = q.index(max(q))
            del q[max_idx]

        else:
            number = int(ch[2:])
            q.append(number)

    if q:
        answer.append(max(q))
        answer.append(min(q))
    else:
        answer.append(0)
        answer.append(0)

    return answer