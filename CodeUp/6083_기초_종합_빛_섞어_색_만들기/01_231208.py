red, green, blue = map(int, input().split())
for r in range(red):
    for g in range(green):
        for b in range(blue):
            print(r, g, b)
print(red * green * blue)
