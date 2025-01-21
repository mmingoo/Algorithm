n = int(input())
info = []

one = 0
two = 0
flag = 0

for i in range(n):
    team, time = input().split()
    m, s = map(int, time.split(':'))

    # 1팀이 득점한 경우
    if team == '1':

        # 득점하기 전에 동점인 경우
        if flag == 0:
            one = 48 * 60 - (m*60 + s)
        flag += 1

        if flag == 0:
            if two > 0:
                two = two - (48 * 60 - ( m * 60 + s))

     # 2팀이 득점한 경우
    else:
        if flag == 0:
            two = 48 * 60 - (m * 60 + s)

        flag -= 1

        if one > 0:
            one = one  -  (48 * 60 - ( m * 60 + s))


print('{:0>2}:{:0>2}'.format(one // 60, one % 60))
print('{:0>2}:{:0>2}'.format(two // 60, two % 60))