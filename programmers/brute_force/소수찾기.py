from itertools import permutations


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return 0
    print(f"{n}일 때 1 추가")
    return 1


def solution(numbers):
    cnt = 0
    permutation_arr = []
    number_arr = []

    for i in range(1, len(numbers) + 1):
        extend_arr = [''.join(map(str, p)) for p in permutations(numbers, i)]
        permutation_arr.extend(extend_arr)

    for i in permutation_arr:
        if int(i) not in number_arr and int(i) != 0 and int(i) != 1:
            number_arr.append(int(i))

    for p in number_arr:
        cnt += is_prime(int(p))

    return cnt