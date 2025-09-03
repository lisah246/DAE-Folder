# Purpose: Sort a list of random numbers so that they are ordered

# Solution/Algorithm: Bubble up the smallest numbers to the front until the list is sorted

# AI Prompt: i am creating a basic code as a beginner backend web development. i want to create code that will help me sort a generic list of random #s so that they are ordered. basically the code will look at the first # and compare it to the second number, if the first number is less than the second # then it stays in that spot, if not, the two #s swap spots, then the code looks at the second # and compares it to the 3rd number, and so on and so on until the list is sorted. can you help me create this code or walk me through how

# # How Bubble Sort Works:
# Compare the first two numbers
# If the first is greater than the second, swap them
# Move to the next pair (second and third numbers)
# Repeat until you reach the end of the list
# Start over from the beginning and repeat the entire process
# Keep doing this until you make a complete pass without any swaps (meaning the list is sorted)
# The algorithm is called "bubble sort" because smaller numbers "bubble up" to the front of the list, just like air bubbles rising to the surface of water.

#Here is the code:

def bubble_sort(numbers):
    """
    Sorts a list of numbers using the bubble sort algorithm.
    
    Args:
        numbers: List of numbers to sort
    
    Returns:
        The sorted list (modifies the original list)
    """
    n = len(numbers)
    
    # We need to make multiple passes through the list
    for i in range(n):
        # Flag to track if any swaps were made in this pass
        swapped = False
        
        # Go through the list, comparing adjacent elements
        # Note: we use (n - i - 1) because after each pass,
        # the largest element "bubbles up" to its correct position
        for j in range(0, n - i - 1):
            # Compare current element with the next one
            if numbers[j] > numbers[j + 1]:
                # Swap if they're in the wrong order
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
                
                # Optional: print to see the swaps happening
                print(f"Swapped {numbers[j + 1]} and {numbers[j]}: {numbers}")
        
        # If no swaps were made, the list is sorted
        if not swapped:
            print("No swaps needed - list is sorted!")
            break
    
    return numbers


# Test Example 1
if __name__ == "__main__":
    # Test with a random list of numbers
    test_numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", test_numbers)
    print("\nSorting process:")
    
    sorted_numbers = bubble_sort(test_numbers.copy())  # Use copy() to keep original unchanged
    
    print(f"\nFinal sorted list: {sorted_numbers}")
    
    # Test Example
    print("\n" + "="*50)
    test_numbers2 = [5, 2, 8, 1, 9]
    print("Original list:", test_numbers2)
    print("\nSorting process:")
    
    sorted_numbers2 = bubble_sort(test_numbers2)
    print(f"\nFinal sorted list: {sorted_numbers2}")