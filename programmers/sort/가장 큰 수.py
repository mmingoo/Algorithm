def solution(numbers):
    new_arr = list(map(str, numbers))
    new_arr.sort(reverse=True, key=lambda x: x * 3)
    return str(int(''.join(new_arr)))




