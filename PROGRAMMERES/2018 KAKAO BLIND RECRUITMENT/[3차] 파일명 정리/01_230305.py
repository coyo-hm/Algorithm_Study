def parseFileName(file):
    num = [str(i) for i in range(0, 10)]
    head = ""
    numbers = ""
    for s in file:
        if s in num:
            numbers += s
        else:
            if len(numbers) == 0:
                head += s
            else:
                return [head.upper(), int(numbers), file]
    return [head.upper(), int(numbers), file]


def solution(files):
    answer = []
    for f in files:
        answer.append(parseFileName(f))
    answer = sorted(answer, key=lambda x: (x[0], x[1]))
    return [f[2] for f in answer]