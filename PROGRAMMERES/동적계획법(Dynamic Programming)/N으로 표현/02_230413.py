def dp(n, num, cnt, res):
    if cnt > 8:
        return 1e9
    if res == num:
        return cnt
    if num - res == 1:
        return cnt + 2 if n != 1 else cnt + 1
    else:
        m = 1e9
        for i in range(1, 7):
            x = int(str(n) * i)
            d = min(dp(n, num,  cnt + i, res - x), dp(n, num,  cnt + i, res + x), dp(n, num,  cnt + i, res * x), dp(n, num,  cnt + i, res // x))
            if d < m:
                m = d
        return m



def solution(N, number):
    ans = dp(N, number, 0, 0)
    return ans if ans <= 8 else -1