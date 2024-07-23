import random
import time

# Define the Knapsack problem parameters
max_weight = 100
"""
items = [
    {"weight": 10, "value": 60},
    {"weight": 20, "value": 100},
    {"weight": 30, "value": 120},
    {"weight": 5, "value": 30},
    {"weight": 25, "value": 80},
    {"weight": 15, "value": 70},
    {"weight": 45, "value": 150},
    {"weight": 8, "value": 50},
    {"weight": 12, "value": 70},
    {"weight": 35, "value": 110},
    {"weight": 40, "value": 160},
    {"weight": 7, "value": 35},
    {"weight": 22, "value": 90},
    {"weight": 18, "value": 75},
    {"weight": 50, "value": 170},
    {"weight": 33, "value": 120},
    {"weight": 28, "value": 95},
    {"weight": 9, "value": 40},
    {"weight": 38, "value": 130},
    {"weight": 14, "value": 55},
    {"weight": 55, "value": 190},
    {"weight": 17, "value": 70},
    {"weight": 42, "value": 160},
    {"weight": 23, "value": 80},
    {"weight": 31, "value": 140},
    {"weight": 20, "value": 75},
    {"weight": 60, "value": 220},
    {"weight": 27, "value": 105},
]
"""
"""
items = [
    {"weight": 10, "value": 60},
    {"weight": 20, "value": 100},
    {"weight": 30, "value": 120},
    {"weight": 5, "value": 30},
    {"weight": 25, "value": 80},
    {"weight": 15, "value": 70},
    {"weight": 45, "value": 150},
]
"""
items = [
    {"weight": 10, "value": 60},
    {"weight": 20, "value": 100},
    {"weight": 30, "value": 120},
    {"weight": 5, "value": 30},
    {"weight": 25, "value": 80},
    {"weight": 15, "value": 70},
    {"weight": 45, "value": 150},
    {"weight": 8, "value": 50},
    {"weight": 12, "value": 70},
    {"weight": 35, "value": 110},
    {"weight": 40, "value": 160},
    {"weight": 7, "value": 35},
    {"weight": 22, "value": 90},
    {"weight": 18, "value": 75},
    {"weight": 50, "value": 170},
    {"weight": 33, "value": 120},
    {"weight": 28, "value": 95},
    {"weight": 9, "value": 40},
    {"weight": 38, "value": 130},
    {"weight": 14, "value": 55},
]

# Genetic Algorithm Parameters
population_size = 100
mutation_rate = 0.1
num_generations = 100

# Create the initial population
def create_individual():
    return [random.choice([0, 1]) for _ in items]

def fitness(individual):
    total_value = 0
    total_weight = 0
    for i in range(len(individual)):
        if individual[i] == 1:
            total_value += items[i]["value"]
            total_weight += items[i]["weight"]
    if total_weight > max_weight:
        return 0
    return total_value

def mutate(individual):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]

def select_parents(population):
    population_with_fitness = [(individual, fitness(individual)) for individual in population]
    population_with_fitness.sort(key=lambda x: x[1], reverse=True)
    return population_with_fitness[:2]

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Initialize the population
population = [create_individual() for _ in range(population_size)]

start_time = time.time()  # Record the start time

# Main genetic algorithm loop
for generation in range(num_generations):
    new_population = []

    for _ in range(population_size // 2):
        parent1, parent2 = select_parents(population)
        child1, child2 = crossover(parent1[0], parent2[0])
        mutate(child1)
        mutate(child2)
        new_population.extend([child1, child2])

    population = new_population

# Calculate and print the fitness of the best individual in this generation
best_individual, best_fitness = select_parents(population)[0]

end_time = time.time()  # Record the end time

print(f"Execution time: {end_time - start_time:.5f} seconds")

print("Final best solution found:")
print("Items selected:", [i for i, bit in enumerate(best_individual) if bit == 1])
print("Total value:", best_fitness)
print("Total weight:", sum(items[i]["weight"] for i, bit in enumerate(best_individual) if bit == 1))
