def solution(n, k, cmd):
    answer = ['O'] * n
    del_row = []
    table = {i: [i - 1 if i - 1 >= 0 else None, i + 1 if i + 1 < n else None] for i in range(n)}
    for i in cmd:
        if i == "C":
            answer[k] = 'X'
            [prev, next] = table[k]
            del_row.append([prev, k, next])
            if next == None:
                k = prev
                table[k][1] = None
            elif prev == None:
                k = next
                table[k][0] = None
            else:
                k = next
                table[prev][1] = next
                table[next][0] = prev

        elif i == "Z":
            [prev, cur, next] = del_row.pop()
            answer[cur] = 'O'
            if prev == None:
                table[next][0] = cur
            elif next == None:
                table[prev][1] = cur
            else:
                table[next][0] = cur
                table[prev][1] = cur
        else:
            [d, m] = i.split(" ")
            m = int(m)
            for i in range(m):
                if d == 'D':
                    k = table[k][1]
                else:
                    k = table[k][0]

    return "".join(answer)