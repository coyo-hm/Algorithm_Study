import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
curr = 0
ans = -1e9

for num in nums:
    curr = max(curr + num, num)
    ans = max(ans, curr)

print(ans)