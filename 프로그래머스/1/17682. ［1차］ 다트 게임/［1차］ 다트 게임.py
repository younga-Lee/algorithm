def solution(dartResult):
    answer = [0]
    i = 0
    while i < len(dartResult):
        # 숫자
        if dartResult[i].isdigit():
            if dartResult[i] == "1" and i + 1 != len(dartResult) and dartResult[i + 1] == "0":  # 10인경우
                tmp = int(10)
                i += 2
            else:
                tmp = int(dartResult[i])
                i += 1
        # 보너스
        if dartResult[i] == 'S':
            i += 1
        elif dartResult[i] == 'D':
            tmp = tmp ** 2
            i += 1
        elif dartResult[i] == 'T':
            tmp = tmp ** 3
            i += 1

        if i == len(dartResult):
            answer.append(tmp)
            break

        # 옵션
        if dartResult[i] == '*':
            answer.append(answer.pop() * 2)
            answer.append(tmp * 2)
            i += 1
        elif dartResult[i] == '#':
            answer.append(tmp * (-1))
            i += 1

        else:
            answer.append(tmp)
    return sum(answer)