import sys

N = int(sys.stdin.readline().strip())
balls = str(sys.stdin.readline().strip())
cnt = []

# 우측으로 레드 모으기
red_right_explore = balls.rstrip('R')
cnt.append(red_right_explore.count('R'))

red_left_explore = balls.lstrip('R')
cnt.append(red_left_explore.count('R'))

blue_right_explore = balls.rstrip('B')
cnt.append(blue_right_explore.count('B'))

blue_left_explore = balls.rstrip('B')
cnt.append(blue_left_explore.count('B'))
print(min(cnt))