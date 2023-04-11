def solution(n):
    arr = [1, 2, 4]
    answer = ''   
    
    while n != 0:
        answer = str(arr[(n - 1) % 3]) + answer        
        n = (n-1) // 3
        
    return answer