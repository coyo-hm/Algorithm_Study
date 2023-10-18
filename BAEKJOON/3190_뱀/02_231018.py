import sys
import collections
input = sys.stdin.readline
n = int(input())
k = int(input())
graph = [[0] * n for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    graph[r - 1][c - 1] = 1
l = int(input())
move = collections.deque([])

for _ in range(l):
    [x, c] = input().split()
    move.append((int(x), c))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
snake = collections.deque([(0, 0)])
snake_dir = 0
time = 0

while True:
    time = time + 1
    nr = snake[0][0] + dr[snake_dir]
    nc = snake[0][1] + dc[snake_dir]
    if nr < 0 or nr >= n or nc < 0 or nc >= n or (nr, nc) in snake:
        break
    # print(time, snake, snake_dir, graph[nr][nc])

    if graph[nr][nc] == 1:
        graph[nr][nc] = 0
    else:
        snake.pop()
    snake.appendleft((nr, nc))
    if move and move[0][0] == time:
        x, c = move[0]
        if c == "L":
            snake_dir = (snake_dir + 3) % 4
        elif c == "D":
            snake_dir = (snake_dir + 1) % 4
        move.popleft()

print(time)