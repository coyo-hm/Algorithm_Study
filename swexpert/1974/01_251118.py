# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5Psz16AYEDFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part2&problemBoxCnt=14
# 00:13:50

PUZZLE_LENGTH = 9


def check_puzzle(puzzle):
    for i in range(PUZZLE_LENGTH):
        if len(set(puzzle[i])) != PUZZLE_LENGTH:
            return 0
        if len(set([puzzle[j][i] for j in range(PUZZLE_LENGTH)])) != PUZZLE_LENGTH:
            return 0

    for sr, sc in [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]:
        temp = set([])
        for i in range(3):
            for j in range(3):
                temp.add(puzzle[sr + i][sr + j])
        if len(temp) != PUZZLE_LENGTH:
            return 0

    return 1


T = int(input())
for test_case in range(1, T + 1):
    puzzle = [list(map(int, input().split())) for _ in range(PUZZLE_LENGTH)]
    print("#{0}".format(test_case), check_puzzle(puzzle))
