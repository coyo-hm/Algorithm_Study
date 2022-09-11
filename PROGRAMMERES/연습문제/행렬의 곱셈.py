def solution(arr1, arr2):
    answer = []
    if len(arr1[0]) != len(arr2):
        arr1, arr2 = arr2, arr1
    R, C, N = len(arr1), len(arr2[0]), len(arr2)
    
    arr2 = list(zip(*arr2))
    
    for r in range(R):
        col = []
        for c in range(C):
            col.append(sum([i * j for i, j in zip(arr1[r], arr2[c])]))
        answer.append(col)

    return answer