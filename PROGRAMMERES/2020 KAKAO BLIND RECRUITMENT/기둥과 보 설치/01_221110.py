def solution(n, build_frame):
    answer = []
    #a는 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
    #b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치를 나타냅니다.
    for [x, y, a, b] in build_frame:
        if x > n or y > n or x < 0 or y < 0:
            continue
        if b == 0:
            if [x, y, a] in answer:
                temp = [i for i in answer if i != [x, y, a]]
                if check(temp):
                    answer = temp
        else:
            temp = answer + [[x, y, a]]
            if check(temp):
                answer = temp   
    answer.sort()
    return answer

def check(list):
    for [x, y, a] in list:
        if a == 0:
            if y == 0:
                continue
            elif [x, y, 1] in list or [x - 1, y, 1] in list:
                continue
            elif [x, y - 1, 0] in list:
                continue
            else:
                return False            
        else:
            if [x, y - 1, 0] in list or [x + 1, y - 1, 0] in list:
                continue
            elif [x + 1, y, 1] in list and [x - 1, y, 1] in list:
                continue
            else:
                return False            
    return True     
        
        