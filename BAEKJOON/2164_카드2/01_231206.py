# https://www.acmicpc.net/problem/2164

import sys
import collections
input = sys.stdin.readline
N = int(input())
cards = collections.deque(range(1, N + 1))

while len(cards) > 1:
    cards.popleft()
    c = cards.popleft()
    cards.append(c)

print(cards[0])