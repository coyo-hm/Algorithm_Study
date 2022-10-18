N, K = map(int, input().split())

cnt = 0
while N >= K:
  if N % K != 0:
    cnt += N % K
    N -= N % K
  N = N // K
  cnt += 1
cnt += (N - 1)

print(cnt)