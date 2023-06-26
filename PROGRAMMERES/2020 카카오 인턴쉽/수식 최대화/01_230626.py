from itertools import permutations

def calc(a, b, arth):
    if arth == "+":
        return a + b
    elif arth == "*":
        return a * b
    else:
        return a - b

def getExp(exp, arth):
    res, a = [], 0
    flag = False
    for e in exp:
        if e == arth:
            a = res.pop()
            flag = True
        elif str(e) not in "-*+" and flag == True:
            res.append(calc(a, int(e), arth))
            flag = False
        else:
            res.append(e)
    return res

def solution(expression):
    arths = []
    n = ""
    express = []
    for e in list(expression):
        if e in "0123456789":
            n += e
        else:
            express.append(int(n))
            express.append(e)
            arths.append(e)
            n = ""
    express.append(n)
    arths = set(arths)
    answer = 0
    for arth in permutations(arths, len(arths)):
        exp = express
        for a in arth:
            exp = getExp(exp, a)
        answer = max(abs(exp[0]), answer)
    return answer