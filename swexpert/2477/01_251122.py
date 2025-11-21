# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV6c6bgaIuoDFAXy&probBoxId=AV732SG66sEDFAW7&type=PROBLEM&problemBoxTitle=%EC%82%BC%EC%84%B1+%EC%8B%A0%EC%9E%85+%EB%AA%A8%EC%9D%98+sw+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AC%B8%EC%A0%9C%EB%AA%A8%EC%9D%8C&problemBoxCnt=10
# 01:46:44


from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N, M, K, A, B = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    t_list = list(map(int, input().split()))

    customer_list = deque([(c, i + 1) for i, c in enumerate(t_list)])
    a_full = [[0, 0]] * N
    b_full = [0] * M
    a_waiting = deque([])
    b_waiting = deque([])
    cnt = 0
    ans_a = set()
    ans_b = set()
    finished = set()
    t = t_list[0]

    while len(finished) < K:
        # print(t, customer_list, a_waiting, a_full, b_waiting, b_full, finished)
        while customer_list:
            time, customer_id = customer_list[0]
            if time <= t:
                a_waiting.append(customer_id)
                customer_list.popleft()
            else:
                break

        for i, [remaining_time, customer_id] in enumerate(a_full):
            if remaining_time != 0:
                a_full[i][0] -= 1
                continue
            if customer_id != 0:
                b_waiting.append(customer_id)
            if len(a_waiting) != 0:
                idx = a_waiting.popleft()
                a_full[i] = [a_list[i] - 1, idx]
                if i == A - 1:
                    ans_a.add(idx)
            else:
                a_full[i][1] = 0

        for i, remaining_time in enumerate(b_full):
            if remaining_time != 0:
                b_full[i] -= 1
                continue
            if len(b_waiting) != 0:
                idx = b_waiting.popleft()
                if i == B - 1:
                    ans_b.add(idx)
                b_full[i] = b_list[i] - 1
                finished.add(idx)

        t += 1

    answer = sum(ans_a - (ans_a - ans_b))
    # print(ans_a, ans_b)
    print("#{0}".format(test_case), answer if answer != 0 else -1)
