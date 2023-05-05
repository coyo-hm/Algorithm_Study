import math
import collections


def solution(progresses, speeds):
    result = []
    dayList = collections.deque([math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))])

    count = 1
    process = dayList.popleft()
    while dayList:
        nextProcess = dayList.popleft()
        if (process >= nextProcess):
            count += 1
        else:
            result.append(count)
            count = 1
            process = nextProcess
    result.append(count)

    return result
