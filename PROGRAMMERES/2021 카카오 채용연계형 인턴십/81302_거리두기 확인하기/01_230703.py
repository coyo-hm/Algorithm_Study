d = [(-2, 0), (-1, 0), (-1, 1), (0, 1), (0, 2),(1, 1), (1, 0), (2, 0), (1, -1), (0, -2), (0, -1), (-1, -1)]

def checkRoom(room):
    for x in range(5):
        for y in range(5):
            if room[x][y] == "P":
                px = []
                for dx, dy in d:
                    nx = dx + x
                    ny = dy + y
                    if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                        continue
                    if room[nx][ny] == "P":
                        if abs(dx) + abs(dy) == 1:
                            # print("case 1", (x, y), (nx, ny))
                            return 0
                        elif nx == x and room[nx][y + dy // 2] == "O":
                            # print("case 2",room[nx][y + dy // 2],  (x, y), (nx, ny))
                            return 0
                        elif ny == y and room[x + dx // 2][ny] == "O":
                            # print("case 3", room[x + dx // 2][ny],(x, y), (nx, ny))
                            return 0
                        elif nx != x and ny != y and (room[nx][y] != "X" or room[x][ny] != "X"):
                            # print("case 4", (x, y), (nx, ny))
                            return 0
    return 1

def solution(places):
    answer = []
    for room in places:
        ans = checkRoom(room)
        answer.append(ans)
    return answer