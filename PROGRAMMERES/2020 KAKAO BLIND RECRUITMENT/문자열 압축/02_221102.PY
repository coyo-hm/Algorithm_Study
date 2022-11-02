def solution(s):    
    answer = len(s)    
    for u in range(1, len(s)):
        piece = ""
        cnt = 1
        res = ""
        i = 0        
        while i < len(s):
            if piece == s[i: i + u]:
                cnt += 1
            else:
                if cnt == 1:
                    res += piece
                else:
                    res += str(cnt) + piece
                    cnt = 1
                piece = s[i: i + u]
            i = i + u
        res += str(cnt) + piece if cnt != 1 else piece
        answer = min(answer, len(res))
    return answer