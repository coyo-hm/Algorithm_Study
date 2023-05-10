import sys
input = sys.stdin.readline
n = int(input())
board = [list(input().rstrip()) for _ in range(n)]
ans = 0
def searchMax(newBoard):
    cnt = 0
    for i in range(n):
        prevX = newBoard[i][0]
        prevY = newBoard[0][i]
        cntX = [1]
        cntY = [1]
        for j in range(1, n):
            if prevX == newBoard[i][j]:
                cntX[-1] += 1
            else:
                cntX.append(1)
                prevX = newBoard[i][j]
            if prevY == newBoard[j][i]:
                cntY[-1] += 1
            else:
                cntY.append(1)
                prevY = newBoard[j][i]
        cnt = max(max(cntX), max(cntY), cnt)
    return cnt

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for x in range(n):
    for y in range(n):
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and board[x][y] != board[nx][ny]:
                temp = board[nx][ny]
                board[nx][ny] = board[x][y]
                board[x][y] = temp
                ans = max(ans, searchMax(board))
                board[x][y] = board[nx][ny]
                board[nx][ny] = temp

print(ans)