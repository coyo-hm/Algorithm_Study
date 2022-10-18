import itertools

N, M= map(int, input().split())
K = list(map(int, input().split()))

result = [i for i in list(itertools.combinations(K, 2)) if i[0] != i[1]]
print(len(result))

