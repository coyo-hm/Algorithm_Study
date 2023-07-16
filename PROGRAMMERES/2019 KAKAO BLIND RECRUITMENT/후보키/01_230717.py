import itertools


def checkUniq(keys, relation, inKeys):
    arr = []
    for r in relation:
        temp = []
        for k in keys:
            temp.append(r[k])

        t = tuple(temp)
        if t in arr:
            return False
        else:
            arr.append(t)
    return True


def validateKey(keys, inKeys):
    for i in range(1, len(keys) + 1):
        if set(itertools.combinations(keys, i)) & set(inKeys):
            return False
    return True


def solution(relation):
    answer = 0
    row_n = len(relation)
    col_n = len(relation[0])
    keys = list(range(col_n))
    inKeys = []

    for i in range(1, col_n + 1):
        if keys == inKeys:
            return answer
        for key in itertools.combinations(keys, i):
            # print(key, answer, inKeys, validateKey(keys, inKeys))
            if validateKey(key, inKeys) and checkUniq(key, relation, inKeys):
                answer += 1
                inKeys.append(key)

    return answer




