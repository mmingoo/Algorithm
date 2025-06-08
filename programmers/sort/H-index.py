def solution(citations):
    result = []
    citations.sort(reverse=True)
    h_idx = 0
    for i in citations:
        if i > h_idx:
            h_idx += 1

    return h_idx