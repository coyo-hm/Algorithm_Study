def solution(word):
    answer = 0
    char = ["", 'A', 'E', 'I', 'O', 'U']
    size = [781, 156, 31, 6, 1]
    wl = len(word)

    for i in range(wl):
        for j in range(1, 6):
            if word[i] == char[j]:
                answer += size[i] * (j - 1)

    return answer + wl