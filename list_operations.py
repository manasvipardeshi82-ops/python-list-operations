numbers = []

for i in range(1, 11):
    value = float(input(f"Enter number {i}: "))
    numbers.append(value)

largest = max(numbers)
smallest = min(numbers)
sum_of_numbers = sum(numbers)
average = sum_of_numbers / len(numbers)

print("\nResults:")
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print(f"Sum of all numbers: {sum_of_numbers}")
print(f"Average of the numbers: {average}")
