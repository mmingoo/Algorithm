"""
1. 아이디어
- 백트래킹 재귀함수 안에서 , for문 돌면서  숫자 선택 (방문 여부 추가)

2. 시간 복잡도
- n! , 최대 10개 까지 가능

3. 자료구조
- bool []
- 결과값 저장 int[]
"""

import sys

input = sys.stdin.readline()

n, m = map(int, input.split())

chk = [False] * (n+1)
rs = []

def recur(num):
    if num == m:
        print(' '.join(map(str, rs)))
        return

    for i in range(1, n+1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            chk[i] = False
            rs.pop()
            recur(num+1)

recur(0)
