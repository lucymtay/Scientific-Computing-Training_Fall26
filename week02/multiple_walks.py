import random

def run_simulation(num_sims):
    final_positions = []   
    for simulation in range(num_sims):
        x = 0
        for step in range(10):
            step = random.choice([-1, 1])
            x += step

        final_positions.append(x)

    average_final_position = sum(final_positions) / len(final_positions)

    # print(f"Final positions after {num_sims} simulations with 10 steps: {final_positions}")
    print(f"Average final position: {average_final_position}")
    return average_final_position

average_5 = run_simulation(5)
average_1000 = run_simulation(1000)
