import random

x = 0
positions = [x]
for i in range(10):
    step = random.choice([-1, 1])
    x += step
    positions.append(x)
    print(f"Step: {step}, Pos: {x}")

print(f"Final Position after 10 steps: {x}")
print(f"All Positions: {positions}")
