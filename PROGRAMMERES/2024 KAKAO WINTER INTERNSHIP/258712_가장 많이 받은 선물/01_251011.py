# https://school.programmers.co.kr/learn/courses/30/lessons/258712?language=python3
# 27:23

def solution(friends, gifts):
    n = len(friends)
    idx = {name: i for i, name in enumerate(friends)}

    # 선물 기록 저장
    give = [[0] * n for _ in range(n)]
    give_cnt = [0] * n
    recv_cnt = [0] * n

    for g in gifts:
        a, b = g.split()
        ai, bi = idx[a], idx[b]
        give[ai][bi] += 1
        give_cnt[ai] += 1
        recv_cnt[bi] += 1

    # 선물 지수 계산
    score = [give_cnt[i] - recv_cnt[i] for i in range(n)]

    # 다음 달에 받을 선물 수
    next_recv = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            a_to_b = give[i][j]
            b_to_a = give[j][i]

            if a_to_b > b_to_a:
                next_recv[i] += 1
            elif b_to_a > a_to_b:
                next_recv[j] += 1
            else:
                if score[i] > score[j]:
                    next_recv[i] += 1
                elif score[j] > score[i]:
                    next_recv[j] += 1
                # 같으면 아무 일도 없음

    return max(next_recv)
