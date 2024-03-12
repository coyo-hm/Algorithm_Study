# https://www.acmicpc.net/problem/5430
# 00:25:45

import sys

input = sys.stdin.readline
from collections import deque


def solutions(nums, commands):
    rt = 0
    for c in commands:
        if c == "R":
            rt += 1
        elif c == "D" and len(nums) == 0:
            print("error")
            return
        elif c == "D" and rt % 2 == 0:
            nums.popleft()
        elif c == "D" and rt % 2 != 0:
            nums.pop()
    nums = list(nums)
    answer = nums if rt % 2 == 0 else nums[::-1]
    print("[" + ",".join(answer) + "]")


for _ in range(int(input())):
    commands = list(input().rstrip())
    n = int(input())
    nums = input().rstrip()[1:-1].split(",")
    nums = nums if n > 0 else []
    nums = deque(nums)
    solutions(nums, commands)
