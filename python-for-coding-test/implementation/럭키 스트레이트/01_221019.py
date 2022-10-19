N = input()
length = len(N)

front = sum([int(i) for i in list(N[0: length // 2])])
back = sum([int(i) for i in list(N[length // 2:])])

result = "LUCKY" if front == back else "READY"

print(result)