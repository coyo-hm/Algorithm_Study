# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5PyTLqAf4DFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part2&problemBoxCnt=14
# 00:03:33

T = int(input())
for test_case in range(1, T + 1):
    word = input().rstrip()
    length = len(word)
    ans = 1
    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            ans = 0
            break

    print("#{0}".format(test_case), ans)
