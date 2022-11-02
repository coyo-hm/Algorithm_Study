def solution(s):
    answer = len(s)
    for i in range(1, len(s)):
        cnt = 1
        temp = s[0: i]
        new = ''
        for j in range(i, len(s), i):
            if (temp == s[j: j + i]): cnt += 1
            else:
                if cnt == 1: new += temp
                else: new += str(cnt) + temp                
                cnt = 1
                temp = s[j: j + i]
            if j + i >= len(s):
              if cnt == 1: new += temp
              else: new += str(cnt) + temp                
              temp = s[j:]
              break;
        answer = min(answer, len(new))
    return answer