def solution(want, number, discount):
    answer = 0
    total_cnt = sum(number)
    for i in range(len(discount) - total_cnt+1):  # 시작점
        flag = 0
        num = number.copy()
        for j in range(i, i + total_cnt):  # total_cnt비교
            pd = discount[j]
            # want비교
            for w in range(len(want)):
                if pd == want[w]:
                    if num[w] == 0:
                        flag = 1
                        break
                    num[w] -= 1
                    break
            else:
                break

            if flag == 1:
                break

        # 날짜를 모두 비교 완료했을 때
        if num == [0] * len(want):
            answer += 1

    return answer