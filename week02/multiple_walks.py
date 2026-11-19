import random

def run_simulation(num_sims, num_steps=10):
    final_positions = []   
    for simulation in range(num_sims):
        x = 0
        for step in range(num_steps):
            step = random.choice([-1, 1])
            x += step

        final_positions.append(x)

    average_final_position = sum(final_positions) / len(final_positions)
    squared_deviations = []
    for position in final_positions:
        deviation = position - average_final_position
        squared_deviation = deviation ** 2
        squared_deviations.append(squared_deviation)

    empirical_variance = sum(squared_deviations) / len(squared_deviations)

    print(f"{num_sims} simulations:")
    print(f"Average final position: {average_final_position}")
    print(f"Empirical variance: {empirical_variance}")
    print(f"Theoretical variance: {num_steps}\n")
    return num_steps, empirical_variance


# Experimenting with the function

# run_simulation(1000, 50)
# run_simulation(1000, 10)
# run_simulation(1000, 100)

step_counts = [10, 20, 50, 100, 200]
empirical_variance = []
theoretical_variance = []

for step in step_counts:
    theoretical_var, empirical_var = run_simulation(1000, step)
    empirical_variance.append(empirical_var)
    theoretical_variance.append(theoretical_var)

import matplotlib.pyplot as plt
plt.plot(step_counts, empirical_variance, label='EmpiricalVariance', marker='o')
plt.plot(step_counts, theoretical_variance, label='TheoreticalVariance', marker='s')
plt.scatter(step_counts, empirical_variance, label="Simulation", color='blue')

plt.xlabel('Number of Steps')
plt.ylabel('Variance of Final Position')
plt.title("Randolm Walk Variance: Empirical vs Theoretical")
plt.legend()
plt.savefig("random_walk_variance.png", dpi=300, bbox_inches="tight")
plt.show()






