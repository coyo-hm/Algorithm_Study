def solution(s):
    r = 0
    for i in range(len(s)):
        temp = []
        rs = s[i:] + s[:i]
        for j in rs:
            if len(temp) != 0 and ((j == ")" and temp[-1] == "(") or (j == "}" and temp[-1] == "{") or (j == "]" and temp[-1] == "[")):
                    temp.pop()
            elif j in ["[", "{", "("]:
                temp.append(j)
            else:
                temp.append(j)
                break;
        if temp == []:
            r += 1
    return r