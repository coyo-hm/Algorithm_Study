def solution(s):
    answer = s
    NUMS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for idx, word in enumerate(NUMS):
        if word in answer:
            answer = answer.replace(word, str(idx))
    return int(answer)