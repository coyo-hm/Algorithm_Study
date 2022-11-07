def solution(key, lock):
    l = len(lock)
    k = len(key)
    new_lock = [[0] * (l * 3) for _ in range(l * 3)]
    
    for i in range(l):
        for j in range(l):
            new_lock[l + i][l + j] = lock[i][j]
    
    for r in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(l * 2):
            for y in range(l * 2):
                for i in range(k):
                    for j in range(k):
                        new_lock[x + i][y + j] += key[i][j]
                if check(new_lock) == True:
                    return True
                for i in range(k):
                    for j in range(k):
                        new_lock[x + i][y + j] -= key[i][j]
    return False

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i -1] = a[i][j]
    return result