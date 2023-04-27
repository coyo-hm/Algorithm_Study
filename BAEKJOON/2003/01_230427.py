import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
l = 0
r = 0
curr = 0

while l < n:
    # print(l, r, curr, cnt)
    if curr > m:
        curr -= nums[l]
        l += 1
    elif curr == m:
        cnt += 1
        if r < n and l < r:
            curr = curr - nums[l] + nums[r]
            l += 1
            r += 1
        else:
            break
    else:
        if r < n:
            curr += nums[r]
            r += 1
        else:
            break

print(cnt)
