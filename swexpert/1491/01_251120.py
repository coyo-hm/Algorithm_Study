# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV2b9AkKACkBBASw&probBoxId=AV-4MojKLNADFATz&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part4&problemBoxCnt=14
# 00:22:06

def calc(N, A, B, r, c):
    return A * abs(r - c) + B * (N - r * c)


T = int(input())
for test_case in range(1, T + 1):
    N, A, B = map(int, input().split())
    answer = int(1e9)

    for n in range(N, 0, -1):
        for i in range(round(n ** 0.5), 0, -1):
            if n % i == 0:
                temp = calc(N, A, B, i, n // i)
                answer = min(temp, answer)
                break

    print("#{0}".format(test_case), answer)
