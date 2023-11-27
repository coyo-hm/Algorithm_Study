import sys
input = sys.stdin.readline
N = int(input())
switch_states = input().split()
S = int(input())
students = [list(map(int, input().split())) for _ in range(S)]

for [g, n] in students:
    if g == 1:
        for i in range(n, N + 1, n):
            switch_states[i - 1] = "1" if switch_states[i - 1] == "0" else "0"
    elif g == 2:
        for i in range(min(n - 1, N - n) + 1):
            if switch_states[n - i - 1] == switch_states[n + i - 1]:
                temp = "1" if switch_states[n - i - 1] == "0" else "0"
                switch_states[n - i - 1] = temp
                switch_states[n + i - 1] = temp
            else:
                break

for i in range(N):
    print(switch_states[i], end=" " if i % 20 != 19 else "\n")