def solution(t, p):
    cnt = 0
    for i in range(len(t)):
        if int(t[i: i + len(p)]) <= int(p) and len(t[i: i + len(p)]) == len(p):
            cnt += 1
    return cnt
    
