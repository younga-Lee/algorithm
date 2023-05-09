import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    
    cnt = 0
    if scoville[0] >= K:
        return cnt
    
    while len(scoville) > 1:
        if scoville[0] >= K:
            return cnt
        heapq.heappush(scoville, heapq.heappop(scoville)+ 2*heapq.heappop(scoville))
        cnt += 1
    
    if heapq.heappop(scoville) >= K:
        return cnt
    return -1