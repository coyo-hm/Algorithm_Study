import heapq

def solution(food_times, k):
    total = sum(food_times)
    
    if total <= k:
        return -1
    
    length = len(food_times)
    foods = [(food_times[i], i + 1) for i in range(length)]
    heapq.heapify(foods)
    
    cnt_rotate = 0
    total_time = 0
    
    
    while total_time + (foods[0][0] - cnt_rotate) * length <= k:
        food = heapq.heappop(foods)[0]
        total_time += (food - cnt_rotate) * length
        cnt_rotate = food      
        length -= 1        
        
    result = sorted(foods, key = lambda x: x[1])
    return result[(k - total_time) % length][1]

