# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV7GKs06AU0DFAXB&probBoxId=AV6kld8aiskDFASb&type=PROBLEM&problemBoxTitle=%EC%82%BC%EC%84%B1%EC%8B%9C%ED%97%98%EB%8C%80%EB%B9%84+%EA%B8%B0%EB%B3%B8%EB%AC%B8%EC%A0%9C%EB%AA%A8%EC%9D%8C%28%EB%82%9C%EC%9D%B4%EB%8F%84+1%7E3%29&problemBoxCnt=15
# 00:50:20

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cnt = 0
    visited_col = [False] * N
    visited_dia1 = [False] * (2 * N - 1)
    visited_dia2 = [False] * (2 * N - 1)


    def place(row):
        global cnt
        if row == N:
            cnt += 1
        for col in range(N):
            if not visited_col[col] and not visited_dia1[row + col] and not visited_dia2[row - col + N - 1]:
                visited_col[col] = True
                visited_dia1[row + col] = True
                visited_dia2[row - col + N - 1] = True
                place(row + 1)
                visited_col[col] = False
                visited_dia1[row + col] = False
                visited_dia2[row - col + N - 1] = False

    place(0)

    # print(route)
    print("#{0}".format(test_case), cnt)
