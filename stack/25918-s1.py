N = int(input())
S = input()
min_day = 0
total = 0

for char in range(len(S)):
    if char == "(":
        total +=1
        min_day += 1

    else:
        total -= 1

    if abs(total) > min_day:
        min_day = abs(total)

if total == 0:
    print(total)
else:
    print(-1)
