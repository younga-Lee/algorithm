def solution(nums):
    N = len(nums)
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                num = nums[i]+nums[j]+nums[k]
                for n in range(2, num):
                    if num%n == 0:
                        break
                else:
                    cnt += 1
    return cnt