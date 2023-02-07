def solution(num_list, n):
    answer = []
    for i in range(len(num_list)//n):
        l = []
        for j in range(i*n, (i+1)*n):
            l.append(num_list[j])
        answer.append(l)
    return answer