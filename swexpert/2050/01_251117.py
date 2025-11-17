# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5QLGxKAzQDFAUq&probBoxId=AV9gdM_anw0DFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part1&problemBoxCnt=20
# 00:03:59

str = input().rstrip()

for s in str:
    ans = ord(s)
    if ans >= ord("A"):
        ans = ans - ord("A") + 1
    else:
        ans = ans - ord("a") + 1
    print(ans, end=" ")