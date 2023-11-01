import sys
input = sys.stdin.readline
P = int(input())

for _ in range(P):
    inputs = list(map(int, input().split()))
    T = inputs[0]
    cnt = 0
    sorted_height = [inputs[1]]

    for m in inputs[2:]:
        included_flag = False
        for idx, n in enumerate(sorted_height):
            if n > m:
                cnt += len(sorted_height[idx:])
                sorted_height.insert(idx, m)
                included_flag = True
                break

        if not included_flag:
            sorted_height.append(m)

    print(T, cnt)