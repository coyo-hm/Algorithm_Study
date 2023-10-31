import sys
from collections import deque
input = sys.stdin.readline
P = int(input())
ans = []

def measure(nums):
    cnt = 0
    arr = nums
    for m in nums:
        temp = deque([m])
        for n in arr:
            if n == m:
                continue
            elif max(temp) > n:
                cnt += len(temp)
                temp.appendleft(n)
            else:
                temp.append(n)
        print(arr)
        print(cnt, m, temp)
        arr = temp
    return cnt


for _ in range(P):
    inputs = list(map(int, input().split()))
    T = inputs[0]
    nums = deque(inputs[1:])
    cnt = measure(nums)
    ans.append(" ".join([str(T), str(cnt)]))

for s in ans:
    print(s)