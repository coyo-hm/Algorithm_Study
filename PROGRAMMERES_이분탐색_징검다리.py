def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance
    rocks.sort()
    while start <= end:
        mid = (start + end) // 2
        del_stonecnt = 0
        start_stone = 0
        # print(mid, answer, start, end, rocks)
        for rock in rocks:
            if rock - start_stone < mid:
                del_stonecnt += 1
            else:
                start_stone = rock
            if del_stonecnt > n:
                break
        if del_stonecnt > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    
    return answer