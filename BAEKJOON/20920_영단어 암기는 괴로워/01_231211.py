import sys
input = sys.stdin.readline
N, M = map(int, input().split())
words_cnt = {}
max_cnt = 1

for _ in range(N):
    word = input().rstrip()
    if len(word) < M:
        continue
    if word in words_cnt:
        words_cnt[word] += 1
        if max_cnt < words_cnt[word]:
            max_cnt = words_cnt[word]
    else:
        words_cnt[word] = 1

cnt = [[] for _ in range(max_cnt + 1)]
for w in words_cnt.keys():
    cnt[words_cnt[w]].append(w)
answer = []
for i in range(max_cnt, -1, -1):
    words = sorted(cnt[i], key=lambda x:[-len(x), x])
    answer.extend(words)

for w in answer:
    print(w)
