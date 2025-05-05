test_case = int(input())

for t in range(1,test_case+1):
    str1 = set(input().strip())
    str2 = input().strip()
    dict = {}


    for ch in str1:
        dict[ch] = 0

    for ch in str2:
        if ch in str1:
            dict[ch]+=1

    max_cnt = max(dict.values())
    print(f"#{t} {max_cnt}")



