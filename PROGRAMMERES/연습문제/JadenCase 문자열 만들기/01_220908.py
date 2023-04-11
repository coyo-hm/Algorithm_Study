def solution(s):
    answer = ""
    w = 0
    for i in s.lower():
        if i == " ":
            answer += " "
            w = 0
        elif w == 0 and (i < "0" or i >"9"):
            answer += i.upper()
            w += 1
        else:
            answer += i
            w += 1
        
    return answer