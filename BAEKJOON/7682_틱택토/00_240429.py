# https://www.acmicpc.net/problem/7682


while True:
    line = input()
    if line == "end":
        break
    line = list(line)
    cnt_x, cnt_o, cnt_dot = 0, 0, 0
    row = [[] for _ in range(3)]
    col = [[] for _ in range(3)]
    for idx, c in enumerate(line):
        row[idx % 3].append(c)
        col[idx // 3].append(c)
        if c == "X":
            cnt_x += 1
        elif c == "O":
            cnt_o += 1
        elif c == ".":
            cnt_dot += 1

    if not(cnt_o + 1 == cnt_x or cnt_x == cnt_o):
        print("invalid")
        continue

    winner = []
    if line[0] == line[4] == line[8]:
        winner.append(line[4])
    if line[2] == line[4] == line[6]:
        winner.append(line[4])
    for i in range(3):
        if len(set(row[i])) == 1:
            winner.append(row[i][0])
        if len(set(col[i])) == 1:
            winner.append(col[i][0])

    cnt_w = len(set(winner))

    if cnt_w > 1:
        print("invalid")
        continue
    if cnt_dot == 0 and len(winner) > 0 and winner[0] == "O":
        print("invalid")
        continue
    if cnt_w == 1 and cnt_o == cnt_x and winner[0] == "X":
        print("invalid")
        continue
    if cnt_w == 1 and cnt_o + 1 == cnt_x and winner[0] == "O":
        print("invalid")
        continue

    print("valid")
