import sys
import collections
input = sys.stdin.readline
t = int(input())


def calc(p, nums):
    nums = collections.deque(nums)
    rt = 0
    for arth in p:
        if arth == "R":
            rt += 1
        elif arth == "D" and len(nums) < 1:
            print("error")
            return
        else:
            if rt % 2 == 0:
                nums.popleft()
            else:
                nums.pop()

    nums = list(map(str, nums))
    if len(nums) == 0:
        print("[]")
    elif rt % 2 == 0:
        print("["+",".join(nums)+"]")
    else:
        print("[" + ",".join(nums[::-1]) + "]")

for _ in range(t):
    p = list(input().rstrip())
    n = int(input())
    nums = input().rstrip()
    nums = list(map(int, nums[1:-1].split(","))) if n > 0 else []
    calc(p, nums)
