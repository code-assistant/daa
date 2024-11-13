class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
    
    def value_per_weight(self):
        return self.value / self.weight

def fractional_knapsack(items, capacity):
    items.sort(key=lambda item: item.value_per_weight(), reverse=True)
    total_value = 0.0
    for item in items:
        if capacity > 0 and item.weight <= capacity:
            capacity -= item.weight
            total_value += item.value
        else:
            fraction = capacity / item.weight
            total_value += item.value * fraction
            break
    return total_value

n = int(input("Enter the number of items: "))
items = []
for i in range(n):
    value = float(input(f"Enter value of item {i + 1}: "))
    weight = float(input(f"Enter weight of item {i + 1}: "))
    items.append(Item(value, weight))

capacity = float(input("Enter the capacity of the knapsack: "))
max_value = fractional_knapsack(items, capacity)
print(f"Maximum value in knapsack = {max_value}")
