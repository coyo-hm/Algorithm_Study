# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV15Khn6AN0CFAYD&probBoxId=AV-4MojKLNADFATz&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part4&problemBoxCnt=14
# 02:04:16

T = int(input())
for test_case in range(1, T + 1):
    _input = input().split()
    num_str, limit = list(_input[0]), int(_input[1])
    visited = set([])
    answer = 0
    n = len(num_str)


    def dfs(curr, cnt):
        global answer
        curr_num = int("".join(curr))
        if (curr_num, cnt) in visited:
            return
        visited.add((curr_num, cnt))

        if cnt == limit:
            answer = max(curr_num, answer)
            return

        for i in range(n):
            for j in range(i + 1, n):
                curr[i], curr[j] = curr[j], curr[i]
                dfs(curr, cnt + 1)
                curr[i], curr[j] = curr[j], curr[i]


    dfs(num_str, 0)
    print("#{0}".format(test_case), answer)
