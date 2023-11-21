def solution(s):
    answer = str(s)
    engNum = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(engNum)):
        if engNum[i] in answer:
            answer = answer.replace(engNum[i], str(i))
    answer = int(answer)
    return answer