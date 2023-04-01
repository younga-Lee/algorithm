def solution(numbers, target):
    global answer
    answer = 0
    N = len(numbers)
    
    def dfs(n, sm):
        global answer
        if n == N:
            if sm == target:
                answer += 1
            return
        dfs(n+1, sm+numbers[n]) #+인 경우
        dfs(n+1, sm-numbers[n]) #-인 경우
    dfs(0, 0)
    
    return answer