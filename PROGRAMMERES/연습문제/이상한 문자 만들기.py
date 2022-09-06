def solution(s):
    cnt = 0
    answer = ""
    for i in s:
        if i == " ":
            cnt = 0
            answer += " "
        elif cnt % 2 == 0:
            cnt += 1
            answer += i.upper()
        else:
            cnt += 1
            answer += i.lower()           
    
    return answer