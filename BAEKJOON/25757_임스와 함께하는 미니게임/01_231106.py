import sys
input = sys.stdin.readline
games = {"Y":2, "F":3, "O":4}
N, type = input().split()
N = int(N)
id_list = [input().rstrip() for _ in range(N)]
id_list = set(id_list)
answer = len(id_list) // (games[type] - 1)
print(answer)