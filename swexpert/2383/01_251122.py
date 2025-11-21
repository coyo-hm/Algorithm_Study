# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5-BEE6AK0DFAVl&probBoxId=AV732SG66sEDFAW7&type=PROBLEM&problemBoxTitle=%EC%82%BC%EC%84%B1+%EC%8B%A0%EC%9E%85+%EB%AA%A8%EC%9D%98+sw+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AC%B8%EC%A0%9C%EB%AA%A8%EC%9D%8C&problemBoxCnt=10
# 01:16:04

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    people, stairs = [], []
    for r in range(N):
        for c in range(N):
            if graph[r][c] == 1:
                people.append((r, c))
            elif graph[r][c] > 1:
                stairs.append((r, c, graph[r][c]))

    def calc_stair_time(stair_idx, arrived_people):
        if len(arrived_people) == 0:
            return 0
        stair_r, stair_c, length = stairs[stair_idx]
        arrived_times = []
        for i in arrived_people:
            people_r, people_c = people[i]
            distance = abs(people_r - stair_r) + abs(people_c - stair_c)
            arrived_times.append(distance + 1)
        arrived_times.sort()
        finish_times = []
        for i, arrived_time in enumerate(arrived_times):
            if i < 3:
                finish_times.append(arrived_time + length)
            else:
                start_time = max(finish_times[i - 3], arrived_time)
                finish_times.append(start_time + length)
        return finish_times[-1]

    total_time = int(1e9)
    num_people = len(people)
    for i in range(1 << num_people):
        stair0 = []
        stair1 = []

        for j in range(num_people):
            if i & (1 << j):
                stair1.append(j)
            else:
                stair0.append(j)

        time0 = calc_stair_time(0, stair0)
        time1 = calc_stair_time(1, stair1)
        curr_total = max(time0, time1)
        # print(curr_total, stair0, stair1)
        if curr_total < total_time:
            total_time = curr_total

    print(f"#{test_case} {total_time}")
