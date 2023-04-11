def solution(land):

    for i in range(1, len(land)):
        for j in range(4):
            temp = land[i - 1][j]
            land[i - 1][j] = -1
            land[i][j] += max(land[i - 1])
            land[i - 1][j] = temp

    return max(land[-1])