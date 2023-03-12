def solution(s):
    t = []
    for w in s:
        if len(t) != 0 and w == t[-1]:
            t.pop()
        else:
            t.append(w)    
    return 1 if len(t) == 0 else 0           