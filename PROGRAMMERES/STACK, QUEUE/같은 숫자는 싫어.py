from collections import deque
def solution(arr):
    q = deque(arr)
    
    answer = [q.popleft()]
    while q:
        element = q.popleft()
        if answer[len(answer) - 1] != element:
            answer.append(element)
    
    return answer