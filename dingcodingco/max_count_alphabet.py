# 첫번째 방법
# def find_max_occurred_alphabet(string):
#     dict = {}
#
#     # 문자 빈도 계산
#     for ch in string:
#         if ch.isalpha():
#             if ch not in dict:
#                 dict[ch] = 1
#             else:
#                 dict[ch] += 1
#
#     # 최대 빈도 찾기
#     max_cnt = max(dict.values())
#
#     # 원본 문자열 순서대로 최대 빈도 문자 찾기
#     for ch in string:
#         if ch.isalpha() and dict[ch] == max_cnt:
#             return ch
#
#
# print("정답 = o 현재 풀이 값 =", find_max_occurred_alphabet("hello my name is dingcodingco"))
# print("정답 = e 현재 풀이 값 =", find_max_occurred_alphabet("we love algorithm"))
# print("정답 = b 현재 풀이 값 =", find_max_occurred_alphabet("best of best youtube"))
#

# 두번째 방법
def find_max_occurred_alphabet(string):
    arr = [0 for i in range(26)]

    for ch in string:
        if ch.isalpha():
            arr[ord(ch.lower()) - 97] += 1

    max_value = max(arr)

    # 원본 문자열 순서대로 최대 빈도 문자 찾기
    for ch in string:
        if ch.isalpha():
            if arr[ord(ch.lower()) - 97] == max_value:
                return ch.lower()

    return None


print("정답 = o 현재 풀이 값 =", find_max_occurred_alphabet("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", find_max_occurred_alphabet("we love algorithm"))
print("정답 = b 현재 풀이 값 =", find_max_occurred_alphabet("best of best youtube"))