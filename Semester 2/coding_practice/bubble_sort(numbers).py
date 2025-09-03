def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

# Use it like this:
my_list = [64, 34, 25, 12, 22, 11, 90]  # Your random numbers go here
sorted_list = bubble_sort(my_list)
print(sorted_list)  # This will print: [11, 12, 22, 25, 34, 64, 90]