import math
def solution(progresses, speeds):
    answer = []
    m = math.ceil((100 - progresses[0]) / speeds[0])
    cnt = 1
    for i in range(1, len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        if day > m:
            answer.append(cnt)
            m = day
            cnt = 1
            if i == (len(progresses) - 1):
                answer.append(cnt)
        else:
            cnt += 1
            if i == (len(progresses) - 1):
                answer.append(cnt)
    return answer