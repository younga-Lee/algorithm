def solution(land):
    dp = [[0] * 4 for _ in range(len(land))]
    
    for i in range(4):
        dp[0][i] = land[0][i]
    
    for i in range(1, len(land)):
        for j in range(4):
            max_score = 0
            for k in range(4):
                if j != k:
                    max_score = max(max_score, dp[i - 1][k] + land[i][j])
            dp[i][j] = max_score
    
    answer = max(dp[-1])
    return answer
