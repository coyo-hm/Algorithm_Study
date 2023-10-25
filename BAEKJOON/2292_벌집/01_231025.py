import sys

input = sys.stdin.readline
n = int(input())
# cnt = [6, 12, 18]
answer = 1
idx = 1
increment = 6

while idx < n:
    answer += 1
    idx += increment
    increment += 6

print(answer)