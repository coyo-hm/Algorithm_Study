def solution(arr):
    m = min(arr)
    return [i for i in arr if i != m] or [-1]