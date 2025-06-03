def solution(genres, plays):
    dict = {}
    lst = []
    result = []
    for i in range(len(genres)):
        if genres[i] in dict:
            dict[genres[i]] += plays[i]
        else:
            dict[genres[i]] = plays[i]
    itmes = list(dict.items())
    for key, value in itmes:
        lst.append((value, key))

    lst.sort(reverse=True)

    for v, k in lst:
        arr = []

        for i in range(len(plays)):
            if genres[i] == k:
                arr.append(([plays[i]], i))
        arr.sort(key = lambda x : (-x[0],x[1]))

        for i in range(len(arr)):
            if i < 2:
                result.append([i][1])

    return result