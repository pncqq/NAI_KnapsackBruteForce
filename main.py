# Przedmiot zawiera wage i wartosc
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


# Generuj itemy na podstawie wag i wartosci
def generate_items(weights, values):
    items = []
    for i in range(len(weights)):
        items.append(Item(weights[i], values[i]))
    return items


# Czy rozwiązanie jest poprawne (czy miesci sie w plecaku)
# Zwraca wartość rozwiązania
def calculate_fitness(solution, items, max_weight):
    total_weight = 0
    total_value = 0
    for i in range(len(solution)):
        if solution[i] == 1:  # jesli w slocie jest przedmiot
            total_weight += items[i].weight  # sumujemy wage plecaka
            total_value += items[i].value  # sumujemy wartosc plecaka
            if total_weight > max_weight:  # jesli przekroczymy wage, zwracamy 0
                return 0
    return total_value


def brute_force(items, max_weight):
    best_fitness = 0
    solution = 0

    # Przechodzimy przez wszystkie mozliwe rozwiazania 2^32
    for i in range(2 ** len(items)):
        print(i)

        solution_string = bin(i)[2:].zfill(len(items))
        solution = [int(digit) for digit in solution_string]

        fitness = calculate_fitness(solution, items, max_weight)
        if fitness > best_fitness:
            best_fitness = fitness
    return solution, best_fitness


max_value = 15
max_weight = 75

weights = [3, 1, 6, 10, 1, 4, 9, 1, 7, 2, 6, 1, 6, 2, 2, 4, 8, 1]
values = [7, 4, 9, 18, 9, 15, 4, 2, 6, 13, 18, 12, 12, 16, 19, 19, 10, 16]

items = generate_items(weights, values)

optimal_solution, optimal_fitness = brute_force(items, max_weight)
print(f"Optymalne rozwiązanie: {optimal_solution}\n"
      f"Optymalna wartość plecaka: {optimal_fitness}")
