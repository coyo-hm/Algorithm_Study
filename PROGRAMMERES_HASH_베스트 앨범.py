def solution(genres, plays):
    answer = []
    temp = [[genres[i], plays[i], i] for i in range(len(genres))]
    temp = sorted(temp, key=lambda x: (x[0], -x[1], x[2]))
    
    g_temp={}
    for g in temp:
        if g[0] not in g_temp: g_temp[g[0]] = g[1]
        else: g_temp[g[0]] += g[1]
        
    g_temp = sorted(g_temp.items(), key = lambda x: -x[1])
    
    for i in g_temp:
        count = 0
        for j in temp:
            if i[0] == j[0]:
                count = count + 1
                if count > 2: break;
                else: answer.append(j[2])
                
    return answer