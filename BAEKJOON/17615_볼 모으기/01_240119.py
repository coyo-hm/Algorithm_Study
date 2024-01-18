# https://www.acmicpc.net/problem/17615
# 00:56:24

import sys

input = sys.stdin.readline

N = int(input())
balls = list(input().rstrip())


def counting(color):
    cnt_front, cnt_back = 0, 0
    is_group = balls[0] == color
    for b in balls:
        if not is_group and b == color:
            cnt_front += 1
        elif is_group and b != color:
            is_group = False

    is_group = balls[-1] == color
    for i in range(N - 1, -1, -1):
        b = balls[i]
        if not is_group and b == color:
            cnt_back += 1
        elif is_group and b != color:
            is_group = False

    return min(cnt_front, cnt_back)


answer = min((counting("B"), counting("R")))
print(answer)
