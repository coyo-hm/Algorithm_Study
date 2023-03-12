def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = ""
        for j in range(n):
            if bin(arr1[i])[2:].zfill(n)[j] == "1" or bin(arr2[i])[2:].zfill(n)[j] == "1":
                a += "#"
            else:
                a += " "              
        
        answer.append(a)
        
    
    
    return answer