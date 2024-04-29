# https://www.acmicpc.net/problem/7682
# 01:17:53

def check(line, o_x):
    if line[0] == line[4] == line[8] == o_x:
        return True
    if line[2] == line[4] == line[6] == o_x:
        return True

    if line[0] == line[1] == line[2] == o_x:
        return True
    if line[3] == line[4] == line[5] == o_x:
        return True
    if line[6] == line[7] == line[8] == o_x:
        return True

    if line[0] == line[3] == line[6] == o_x:
        return True
    if line[1] == line[4] == line[7] == o_x:
        return True
    if line[2] == line[5] == line[8] == o_x:
        return True

    return False


while True:
    line = input()
    if line == "end":
        break
    line = list(line)
    cnt_x, cnt_o, cnt_dot = 0, 0, 0
    for c in line:
        if c == "X":
            cnt_x += 1
        elif c == "O":
            cnt_o += 1
        elif c == ".":
            cnt_dot += 1

    if not(cnt_o + 1 == cnt_x or cnt_x == cnt_o):
        print("invalid")
        continue

    if cnt_o == cnt_x and check(line, "O") and not check(line, "X"):
        print("valid")
        continue

    if cnt_o + 1 == cnt_x and not check(line, "O") and check(line, "X"):
        print("valid")
        continue

    if cnt_dot == 0 and not check(line, "O") and not check(line, "X"):
        print("valid")
        continue
    print("invalid")

