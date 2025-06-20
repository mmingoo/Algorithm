from itertools import permutations


def solution(k, dungeons):
    visited = 0
    for dungeon_permutation in permutations(dungeons):
        have = k
        cnt = 0

        for arr in dungeon_permutation:
            min_heart, cost = arr[0], arr[1]

            if have >= arr[0]:
                have -= cost
                cnt += 1
        visited = max(visited, cnt)

    return visited