days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
t = int(input())
for tc in range(1,t+1):

    a_month, a_day , b_month , b_day = map(int,input().split())
    result = 0

    if a_month == b_month:
        result += abs(a_day - b_day) + 1

    else:
        for i in range(a_month, b_month+1):
            if i == a_month:
                result += (days[a_month] - a_day + 1)
            elif i == b_month:

                result += b_day
            else:
                result+=days[i]

    print(f'#{tc} {result}')
