def solution(numbers, hand):
    answer = ''
    phone = []
    for i in range(1, 10, 3):
        tmp = []
        for j in range(3):
            tmp.append(i + j)
        phone.append(tmp)
    phone += [[10, 11, 12]]

    r, l = [12], [10]
    for num in numbers:
        if num in [1, 4, 7]:
            l.append(num)
            answer += 'L'
        elif num in [3, 6, 9]:
            r.append(num)
            answer += 'R'
        else:
            r_num = r[-1]
            l_num = l[-1]
            if num == 0:
                num = 11
            r_cnt, l_cnt = 0, 0
            if r_num not in [2,5,8,11]:
                r_cnt += 1
                r_cnt += abs(r_num-1-num)//3
            else:
                r_cnt += abs(r_num-num)//3

            if l_num not in [2,5,8,11]:
                l_cnt += 1
                l_cnt += abs(l_num+1-num)//3
            else:
                l_cnt += abs(l_num-num)//3

            if l_cnt < r_cnt:
                l.append(num)
                answer += 'L'
            elif l_cnt > r_cnt:
                r.append(num)
                answer += 'R'
            else:
                if hand == 'right':
                    r.append(num)
                    answer += 'R'
                else:
                    l.append(num)
                    answer += 'L'
    return answer
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"	))