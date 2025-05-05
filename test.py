answer = 0
prono = ['aya', 'ye', 'woo', 'ma']
babbling = ["aya", "yee", "u", "maa", "wyeoo"]
for i in babbling:
    for j in prono:
        if j + j in i:  # 같은 발음이 연속되는지 체크 (j+j 대신 j*2 사용)
            print(j * 2)
            break
        else:
            i = i.replace(j, "").strip()

    if i:  # 문자열이 남아있으면
        continue
    else:  # 문자열이 완전히 비어있으면
          # 디버깅용 출력
        answer += 1
print(answer)