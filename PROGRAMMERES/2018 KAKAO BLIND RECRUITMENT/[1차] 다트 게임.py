import re
import math

def solution(dartResult):
    scores = list(map(int, re.findall(r'\d+', dartResult)))
    cnt = 0
    
    for i in range(len(dartResult)):        
        if('0' <= dartResult[i] and dartResult[i] <= "9"):
            continue;
        elif dartResult[i] == "S":
            if i + 1 < len(dartResult) and (dartResult[i + 1] != "*" and dartResult[i + 1] != "#"):
                cnt += 1
        elif dartResult[i] == "D":
            scores[cnt] = math.pow(scores[cnt], 2)
            if i + 1 < len(dartResult) and (dartResult[i + 1] != "*" and dartResult[i + 1] != "#"):
                cnt += 1
            
        elif dartResult[i] == "T":
            scores[cnt] = math.pow(scores[cnt], 3)
            if i + 1 < len(dartResult) and (dartResult[i + 1] != "*" and dartResult[i + 1] != "#"):
                cnt += 1
        elif dartResult[i] == "*":
            scores[cnt] = scores[cnt] * 2
            if cnt != 0:
                scores[cnt - 1] = scores[cnt - 1] * 2
            cnt += 1
        elif dartResult[i] == "#":
            scores[cnt] = scores[cnt] * -1
            cnt += 1        
        
    
    return sum(scores)