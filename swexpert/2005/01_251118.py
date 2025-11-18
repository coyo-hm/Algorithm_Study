# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5P0-h6Ak4DFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part2&problemBoxCnt=14
# 00:16:21

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    print("#{0}".format(test_case))
    prev = []
    curr = []
    for i in range(n):
        for j in range(1, i):
            temp = 1
            if 0 < j < i:
                temp = prev[j] + prev[j - 1]
            curr.append(temp)
        curr.append(1)
        print(" ".join(map(str, curr)))
        prev = curr.copy()
        curr = [1]
