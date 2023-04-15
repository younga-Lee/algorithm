def solution(brown, yellow):
    total = brown + yellow
    
    for i in range(total+1, 0, -1):
        if total%i == 0:
            a = i
            b = total//a
            if (a-2)*(b-2) == yellow:
                return a, b