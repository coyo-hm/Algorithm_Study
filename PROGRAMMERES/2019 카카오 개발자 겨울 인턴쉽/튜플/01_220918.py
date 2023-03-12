def solution(s):
    l = sorted([i.replace("}","") for i in s[1:-1].replace("{","").split("},")], key=len)    
    answer = []
    for i in l:
        for j in i.split(","):
            if int(j) not in answer:
                answer.append(int(j))
    return answer