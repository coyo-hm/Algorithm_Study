def solution(routes):
    routes.sort()
    answer = [routes[0]]
    for i in range(1, len(routes)):
        [s, e] = answer[-1]
        if routes[i][0] <= e:
            answer[-1] = [routes[i][0], routes[i][1] if routes[i][1] <= e else e]
        else:
            answer.append(routes[i])
    return len(answer)