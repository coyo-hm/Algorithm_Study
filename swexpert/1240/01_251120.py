# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV15FZuqAL4CFAYD&probBoxId=AV-4MojKLNADFATz&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part4&problemBoxCnt=14
# 00:30:00


CODE_LENGTH = 56

DECODE_GRID = [
    "0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"
]


def check(code):
    odd, even = 0, 0
    for i, n in enumerate(code):
        if i % 2 == 0:
            odd += n
        else:
            even += n
    return (odd * 3 + even) % 10 == 0


def find_code(graph, n, m):
    for r in range(n):
        if len(set(graph[r])) == 1:
            continue
        for c in range(m - 1, -1, -1):
            if graph[r][c] == "1":
                return graph[r][c - CODE_LENGTH + 1:c + 1]
                # return r, c - CODE_LENGTH + 1


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(n)]
    code_str = find_code(graph, n, m)
    decode = []
    for i in range(0, CODE_LENGTH, 7):
        code = "".join(code_str[i:i + 7])
        for j in range(10):
            if code == DECODE_GRID[j]:
                decode.append(j)
                break
    print("#{0}".format(test_case), sum(decode) if check(decode) else 0)
