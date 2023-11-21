from collections import deque


def solution(n, k, cmd):
    chart = ["O"] * n
    delete = deque([])
    up = [i - 1 for i in range(n)]
    down = [i + 1 for i in range(n - 1)] + [-1]

    for c in cmd:
        if "U" in c:
            x = int(c.split(" ")[1])
            while x > 0:
                k = up[k]
                x -= 1
        elif "D" in c:
            x = int(c.split(" ")[1])
            while x > 0:
                k = down[k]
                x -= 1
        elif "C" in c:
            chart[k] = "X"
            delete.append(k)
            if up[k] != -1:
                down[up[k]] = down[k]
            if down[k] != -1:
                up[down[k]] = up[k]
            k = down[k] if down[k] != -1 else up[k]
        elif "Z" in c:
            if len(delete) != 0:
                d = delete.pop()
                chart[d] = "O"
                if down[d] != -1:
                    up[down[d]] = d
                if up[d] != -1:
                    down[up[d]] = d
    return "".join(chart)