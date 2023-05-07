def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    for idx, n in enumerate(numbers):
        while stack and numbers[stack[-1]] < n:
            answer[stack.pop()] = n
        stack.append(idx)

    return answer