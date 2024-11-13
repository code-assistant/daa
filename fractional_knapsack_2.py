def fractional_knapsack(values, weights, capacity):
    items = [(values[i], weights[i], values[i] / weights[i]) for i in range(len(values))]
    items.sort(key=lambda item: item[2], reverse=True)
    
    total_value = 0.0
    for value, weight, ratio in items:
        if capacity > 0 and weight <= capacity:
            capacity -= weight
            total_value += value
        else:
            fraction = capacity / weight
            total_value += value * fraction
            break
    
    return total_value

n = int(input("Enter the number of items: "))
values = []
weights = []

for i in range(n):
    value = float(input(f"Enter value of item {i + 1}: "))
    weight = float(input(f"Enter weight of item {i + 1}: "))
    values.append(value)
    weights.append(weight)

capacity = float(input("Enter the capacity of the knapsack: "))
max_value = fractional_knapsack(values, weights, capacity)
print(f"Maximum value in knapsack = {max_value}")
