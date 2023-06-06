def checkPress(sx, sy, s, arr):
    flag = arr[sx][sy]
    if s * s == sum([arr[x][sy:sy + s] for x in range(sx, sx + s)], []).count(flag):
        for x in range(sx, sx + s):
            for y in range(sy, sy + s):
                arr[x][y] = -1
        return flag
    else:
        return -1


def solution(arr):
    answer = [0, 0]
    s = len(arr)
    n = len(arr)
    while s > 0:
        for x in range(0, n, s):
            for y in range(0, n, s):
                res = checkPress(x, y, s, arr)
                if res == 1:
                    answer[1] += 1
                elif res == 0:
                    answer[0] += 1
        s = s // 2
        # print(arr, s)
    return answer