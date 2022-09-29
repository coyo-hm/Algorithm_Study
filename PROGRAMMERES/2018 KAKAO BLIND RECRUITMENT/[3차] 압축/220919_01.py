def solution(msg):
    dic = ["A", 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    answer = []
    temp = ""
    for i in msg:
        if temp + i in dic:
            temp += i
        else:
            answer.append(dic.index(temp) + 1)
            dic.append(temp + i)
            temp = i
    answer.append(dic.index(temp) + 1)
    return answer