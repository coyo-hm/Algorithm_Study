def solution(elements):
    eLen = len(elements)
    answer = set()
    elements = elements * 2
    for i in range(eLen):
        for j in range(eLen):
            answer.add(sum(elements[i:i+j+1]))
    return len(answer)