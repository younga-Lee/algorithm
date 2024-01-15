def solution(arr1, arr2):
    a1 = len(arr1)
    a2 = len(arr1[0])
    b2 = len(arr2[0])
    answer = [[0]*b2 for _ in range(a1)]
    
    for i in range(a1):
        for j in range(b2):
            sm = 0
            for k in range(a2):
                sm += arr1[i][k]*arr2[k][j]
            answer[i][j] = sm
    
    return answer