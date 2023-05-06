def solution(absolutes, signs):
    return sum(list(map(lambda x: absolutes[x]*-1 if signs[x] == False else absolutes[x], [i for i in range(len(signs))])))