import math


def solution(n, k):
    nums = list(range(1, n + 1))
    ans = []
    for i in range(n - 1, -1, -1):
        num = math.factorial(i)
        idx = k // num
        k = k % num
        if k == 0:
            ans.append(nums.pop(idx - 1))
        else:
            ans.append(nums.pop(idx))

    return ans