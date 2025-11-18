# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5PpoFaAS4DFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part2&problemBoxCnt=14
# 00:08:33

def solution(a_len, b_len, a_list, b_list):
    answer = 0
    for b in range(b_len - a_len + 1):
        temp = 0
        for a in range(a_len):
            temp += a_list[a] * b_list[b + a]
        answer = max(answer, temp)

    return answer


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    answer = 0

    if n > m:
        answer = solution(m, n, b_list, a_list)
    else:
        answer = solution(n, m, a_list, b_list)

    print("#{0}".format(test_case), answer)
