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
def knapsack_bruteforce(items, max_weight):
    n = len(items)
    best_value = 0
    best_combination = []

    start_time = time.time()  # Record the start time

    for i in range(2 ** n):
        combination = [int(bit) for bit in format(i, f'0{n}b')]
        total_weight = sum(combination[j] * items[j]["weight"] for j in range(n))
        total_value = sum(combination[j] * items[j]["value"] for j in range(n))

        if total_weight <= max_weight and total_value > best_value:
            best_value = total_value
            best_combination = combination

    end_time = time.time()  # Record the end time

    selected_items = [i for i, bit in enumerate(best_combination) if bit == 1]
    return best_value, selected_items, end_time - start_time

best_value, selected_items, execution_time = knapsack_bruteforce(items, max_weight)

print("Best solution found using brute force:")
print("Items selected:", selected_items)
print("Total value:", best_value)
print("Total weight:", sum(items[i]["weight"] for i in selected_items))
print("Execution time:", execution_time, "seconds")
