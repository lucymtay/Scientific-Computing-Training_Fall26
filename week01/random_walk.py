steps = [1, -1, -1, 1, 1, 1, -1]
x = 0
result = [x]

for step in steps:
    x += step
    result.append(x)
print(result)


