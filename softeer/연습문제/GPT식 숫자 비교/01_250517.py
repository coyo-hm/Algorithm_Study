# https://softeer.ai/practice/11001
import sys
input = sys.stdin.readline
N = int(input())
nums = [input().strip() for _ in range(N)]
# print(nums)
nums.sort(key=lambda x: (int(x.split(".")[0]), int(x.split(".")[1]) if "." in x else 0, "." in x))
for n in nums:
    print(n)