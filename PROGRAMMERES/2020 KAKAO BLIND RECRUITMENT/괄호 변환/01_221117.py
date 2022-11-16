def check_balance(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i

def check_proper(u):
    cnt = 0
    for i in u:
        if i == "(":
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return cnt == 0

def solution(p):
    if len(p) == 0:
        return ''
    idx = check_balance(p)
    u = p[0 : idx + 1]
    v = p[idx + 1:]    
    answer = ''
    
    if check_proper(u):
        answer = u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("
        answer += "".join(u)
        
    return answer
