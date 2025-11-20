# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV14Rq5aABUCFAYi&probBoxId=AV-4MojKLNADFATz&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part4&problemBoxCnt=14
# 30:44

UNIT = 100
# UNIT = 8


def get_max_length(sentence):
    length = 0
    # print(sentence)
    for m in range(1, UNIT - 2):
        temp = 1
        # print(length, "mid", m, ":", end=" ")
        for i in range(1, UNIT):
            if m - i < 0 or m + i >= UNIT:
                break
            # print((i, temp), (sentence[m - i], sentence[m + i]), end=" ")
            if sentence[m + i] != sentence[m - i]:
                break
            else:
                temp += 2
        length = max(temp, length)
        # print()
    for m in range(0, UNIT - 1):
        if sentence[m] != sentence[m + 1]:
            continue
        temp = 2
        for i in range(1, UNIT):
            l, r = m - i, m + 1 + i
            if l < 0 or r >= UNIT:
                break
            if sentence[l] != sentence[r]:
                break
            else:
                temp += 2
        length = max(temp, length)

    return length


T = 10
# T = 1
for _ in range(1, T + 1):
    test_case = int(input())
    graph = [list(input().rstrip()) for _ in range(UNIT)]
    answer = 0
    for i in range(UNIT):
        # print("row", i)
        row_max = get_max_length(graph[i])
        col_max = get_max_length([graph[j][i] for j in range(UNIT)])
        answer = max(row_max, col_max, answer)
    print("#" + str(test_case), answer)
