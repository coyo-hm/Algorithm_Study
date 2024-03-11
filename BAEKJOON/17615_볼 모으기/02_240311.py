# https://www.acmicpc.net/problem/17615
# 00:21:30

import sys

input = sys.stdin.readline

n = int(input())
balls = list(input().rstrip())


def counter(color):
    cnt_back, cnt_front = 0, 0
    is_group = balls[0] == color
    for i in range(n):
        if not is_group and balls[i] == color:
            cnt_front += 1
        elif is_group and balls[i] != color:
            is_group = False

    is_group = balls[-1] == color
    for i in range(n - 1, -1, -1):
        if not is_group and balls[i] == color:
            cnt_back += 1
        elif is_group and balls[i] != color:
            is_group = False

    return min(cnt_front, cnt_back)


answer = min(counter("B"), counter("R"))
print(answer)
