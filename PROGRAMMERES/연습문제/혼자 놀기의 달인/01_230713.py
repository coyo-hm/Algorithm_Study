from collections import Counter


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(cards):
    answer = 0
    parents = [i for i in range(len(cards) + 1)]
    for i in range(len(cards)):
        union_parent(parents, i + 1, cards[i])

    for i in range(1, len(cards) + 1):
        find_parent(parents, i)

    nums = list(Counter(parents).values())
    nums.sort(reverse=True)

    # print(nums)
    return nums[0] * nums[1] if len(nums) > 2 else 0