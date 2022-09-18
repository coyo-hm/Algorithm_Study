def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    A = [str1[a:a + 2] for a in range(len(str1) - 1) if str1[a] >= "a" and str1[a] <= "z" and str1[a + 1] >= "a" and str1[a + 1] <= "z"]
    B = [str2[a:a + 2] for a in range(len(str2) - 1) if str2[a] >= "a" and str2[a] <= "z" and str2[a + 1] >= "a" and str2[a + 1] <= "z"]
    i  = []
    a, b = len(A), len(B)
    for j in A:
        if j in B:
            B.remove(j)
            i.append(j)
            
        
    
    answer = len(i) / (a + b - len(i)) if (a + b - len(i)) != 0 else 1
    # print(A, B, i)
    return int(answer * 65536)
