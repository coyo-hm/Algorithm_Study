import heapq
def solution(n, works):
    max_heap = []
    for w in works:
        heapq.heappush(max_heap, (-w, w))
        
    for _ in range(n):
        w = heapq.heappop(max_heap)
        if w[1] == 0:
            break
        new_value = w[1] - 1
        heapq.heappush(max_heap, (-new_value, new_value))
            
    answer = 0
    for i in max_heap:
        answer += i[1]*i[1]
        
    return answer