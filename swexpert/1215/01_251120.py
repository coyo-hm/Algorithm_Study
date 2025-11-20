# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV14QpAaAAwCFAYi&probBoxId=AV-4MojKLNADFATz&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part4&problemBoxCnt=14
# 00:16:17


UNIT = 8


def get_count(sentence, length):
    count = 0
    if length % 2 == 0:
        for m in range(0, UNIT - 1):
            if sentence[m] != sentence[m + 1]:
                continue
            l, r, temp = m - 1, m + 2, 2
            while l >= 0 and r < UNIT and temp <= length:
                if sentence[l] != sentence[r]:
                    break
                else:
                    temp += 2
                    l -= 1
                    r += 1
            if length in [temp, temp - 2]:
                count += 1
    else:
        for m in range(0, UNIT - 1):
            l, r, temp = m - 1, m + 1, 1
            while l >= 0 and r < UNIT and temp <= length:
                if sentence[l] != sentence[r]:
                    break
                else:
                    temp += 2
                    l -= 1
                    r += 1
            if length in [temp, temp - 2]:
                count += 1

    return count


T = 10
for test_case in range(1, T + 1):
    count = int(input())
    graph = [list(input().rstrip()) for _ in range(UNIT)]
    answer = 0
    for i in range(UNIT):
        row_cnt = get_count(graph[i], count)
        col_cnt = get_count([graph[j][i] for j in range(UNIT)], count)
        answer += row_cnt + col_cnt
    print("#" + str(test_case), answer)