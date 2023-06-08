def solution(food):
    answer = '0'
    for i in range(len(food) - 1, 0, -1):
        cnt = food[i] // 2
        if cnt > 0:
            answer = str(i) * cnt + answer + str(i) * cnt
    return answer